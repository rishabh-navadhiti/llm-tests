from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import json
import time
import requests
import re
import os
from datetime import datetime
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global generation parameters (not exposed to frontend)
TEMPERATURE = 0.1
TOP_P = 0.3
MAX_TOKENS = 4000
FREQUENCY_PENALTY = 0.0
PRESENCE_PENALTY = 0.0

# Local vLLM server configuration
VLLM_API_URL = "http://localhost:8000/v1/chat/completions"

# Request Models
class MedicalNoteRequest(BaseModel):
    system_prompt: str = Field(..., description="System instructions for the model")
    json_template: Dict[str, Any] = Field(..., description="JSON template to populate")
    medical_transcript: List[Dict[str, str]] = Field(..., description="Transcript as list of speaker/conversation objects")
    recording_id: Optional[str] = Field(None, description="Optional ID for saving test files")

class TokenUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

class TimingInfo(BaseModel):
    total_time_ms: float
    generation_time_ms: float
    processing_time_ms: float

class MedicalNoteResponse(BaseModel):
    success: bool
    generated_json: Optional[Dict[str, Any]] = None
    token_usage: Optional[TokenUsage] = None
    timing: Optional[TimingInfo] = None
    error_message: Optional[str] = None

# FastAPI App
app = FastAPI(
    title="Medical Note Generation API",
    description="API for generating structured medical notes from transcripts using Qwen 30B A3B Instruct",
    version="1.0.0"
)

def format_transcript(transcript_data: List[Dict[str, str]]) -> str:
    """Format transcript JSON into a readable string with speaker labels."""
    formatted_transcript = ""
    for entry in transcript_data:
        speaker = entry.get("speaker", "unknown").capitalize()
        conversation = entry.get("conversation", "")
        formatted_transcript += f"{speaker}: {conversation}\n"
    
    return formatted_transcript.strip()

def build_medical_prompt(system_prompt: str, json_template: Dict[str, Any], formatted_transcript: str) -> str:
    """Build the complete prompt for medical note generation."""
    template_str = json.dumps(json_template, indent=2, ensure_ascii=False)
    
    prompt = (
        f"{system_prompt}\n\n"
        "### JSON TEMPLATE TO POPULATE:\n"
        f"{template_str}\n\n"
        "### INSTRUCTIONS:\n"
        "Extract information from the medical transcript below and populate the JSON template. "
        "Be precise and only include information that is explicitly mentioned in the transcript. "
        "Do not add any information that is not present in the transcript.\n\n"
        "### MEDICAL TRANSCRIPT:\n"
        f"{formatted_transcript}\n\n"
        "### OUTPUT:\n"
        "Return ONLY valid JSON that matches the template structure above. "
        "Do not include any explanations, commentary, or additional text outside the JSON structure."
    )
    
    return prompt

def extract_json_from_response(response: str) -> Optional[Dict[str, Any]]:
    """
    Extract JSON from model response, handling various formatting issues.
    """
    if not response or not response.strip():
        return None
    
    # Try direct parsing first
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass
    
    # Try to find JSON in the response using various patterns
    patterns = [
        r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}',  # JSON object
        r'```json\s*(\{.*?\})\s*```',  # JSON in code block with language
        r'```\s*(\{.*?\})\s*```',  # JSON in code block without language
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue
    
    # Try to find the outermost JSON structure by counting braces
    brace_level = 0
    start_idx = -1
    
    for i, char in enumerate(response):
        if char == '{':
            if brace_level == 0:
                start_idx = i
            brace_level += 1
        elif char == '}':
            brace_level -= 1
            if brace_level == 0 and start_idx >= 0:
                candidate = response[start_idx:i+1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    continue
    
    return None

def save_test_files(recording_id: str, prompt: str, raw_response: str, extracted_json: Dict[str, Any]):
    """
    Save test files for debugging purposes.
    Creates a folder with the recording_id and saves three files:
    1. input.txt - contains the prompt
    2. raw_output.json - contains the raw response from vLLM
    3. processed_output.json - contains the extracted JSON
    """
    try:
        # Create directory if it doesn't exist
        test_dir = Path(f"test_outputs/{recording_id}")
        test_dir.mkdir(parents=True, exist_ok=True)
        
        # Save input prompt
        with open(test_dir / "input.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        
        # Save raw response
        with open(test_dir / "raw_output.json", "w", encoding="utf-8") as f:
            json.dump({"response": raw_response}, f, indent=2, ensure_ascii=False)
        
        # Save processed JSON
        with open(test_dir / "processed_output.json", "w", encoding="utf-8") as f:
            json.dump(extracted_json, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved test files for recording_id: {recording_id}")
    except Exception as e:
        logger.error(f"Error saving test files: {e}")

@app.get("/")
async def root():
    return {"message": "Medical Note Generation API", "status": "healthy"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.post("/generate-medical-note", response_model=MedicalNoteResponse)
async def generate_medical_note(request: MedicalNoteRequest):
    """
    Generate a structured medical note from a transcript using Qwen 30B A3B Instruct.
    """
    total_start_time = time.time()
    
    try:
        # Format the transcript
        formatted_transcript = format_transcript(request.medical_transcript)
        
        # Build the prompt
        prompt = build_medical_prompt(
            request.system_prompt, 
            request.json_template, 
            formatted_transcript
        )
        
        # Prepare messages for the model
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        # Call local vLLM server
        generation_start_time = time.time()
        
        payload = {
            "model": "Qwen/Qwen3-30B-A3B-Instruct",
            "messages": messages,
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "max_tokens": MAX_TOKENS,
            "frequency_penalty": FREQUENCY_PENALTY,
            "presence_penalty": PRESENCE_PENALTY,
            "stream": False
        }
        
        response = requests.post(VLLM_API_URL, json=payload, timeout=300)
        response.raise_for_status()
        
        vllm_response = response.json()
        generation_time_ms = (time.time() - generation_start_time) * 1000
        
        # Extract the response content
        choices = vllm_response.get("choices", [])
        if not choices:
            raise HTTPException(status_code=500, detail="No choices returned from model")
        
        content = choices[0].get("message", {}).get("content", "")
        
        # Extract token usage information
        usage_data = vllm_response.get("usage", {})
        token_usage = TokenUsage(
            prompt_tokens=usage_data.get("prompt_tokens", 0),
            completion_tokens=usage_data.get("completion_tokens", 0),
            total_tokens=usage_data.get("total_tokens", 0)
        )
        
        # Extract JSON from the response
        processing_time_start = time.time()
        extracted_json = extract_json_from_response(content)
        processing_time_ms = (time.time() - processing_time_start) * 1000
        
        # Calculate total time
        total_time_ms = (time.time() - total_start_time) * 1000
        
        # Save test files if recording_id is provided
        if request.recording_id:
            save_test_files(request.recording_id, prompt, content, extracted_json or {})
        
        # Prepare timing information
        timing_info = TimingInfo(
            total_time_ms=total_time_ms,
            generation_time_ms=generation_time_ms,
            processing_time_ms=processing_time_ms
        )
        
        # Return successful response
        return MedicalNoteResponse(
            success=True,
            generated_json=extracted_json,
            token_usage=token_usage,
            timing=timing_info
        )
        
    except Exception as e:
        logger.error(f"Error generating medical note: {e}")
        return MedicalNoteResponse(
            success=False,
            error_message=str(e)
        )

# For testing locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)  # Different port than vLLM