from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import json
import time
import requests
import re
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DETAILS_LOG_PATH = "/workspace/llm-tests/fastapi/details.json"


# generation parameters 
MODEL = "Qwen/Qwen3-30B-A3B-Instruct-2507-FP8"
TEMPERATURE = 0.1
TOP_P = 0.3
MAX_TOKENS = 6000
FREQUENCY_PENALTY = 0.0
PRESENCE_PENALTY = 0.0

VLLM_API_URL = "http://localhost:8000/v1/chat/completions"

# Request Models
class MedicalNoteRequest(BaseModel):
    system_prompt: str
    json_template: List[Dict[str, Any]] 
    medical_transcript: List[Dict[str, str]]
    recording_id: Optional[str] = None

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
    generated_json: Optional[List[Dict[str, Any]]] = None  
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

def build_medical_prompt(system_prompt: str, json_template: List[Dict[str, Any]], formatted_transcript: str) -> str:
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

def extract_json_from_response(response: str) -> Optional[Any]:
    """
    Extract JSON (list or dict) from model response, handling various formatting issues.
    Returns either a dict or list depending on what the model output is.
    """
    if not response or not response.strip():
        return None

    # Direct parse
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        pass

    # Regex patterns for arrays and objects
    patterns = [
        r'```json\s*([\s\S]*?)```',   
        r'```\s*([\s\S]*?)```',       
        r'(\[.*\])',                  
        r'(\{.*\})',                  
    ]

    for pattern in patterns:
        matches = re.findall(pattern, response, re.DOTALL)
        for match in matches:
            try:
                return json.loads(match)
            except json.JSONDecodeError:
                continue

    # Fallback: try brace/bracket balancing
    for open_char, close_char in [('{', '}'), ('[', ']')]:
        level = 0
        start_idx = -1
        for i, char in enumerate(response):
            if char == open_char:
                if level == 0:
                    start_idx = i
                level += 1
            elif char == close_char:
                level -= 1
                if level == 0 and start_idx >= 0:
                    candidate = response[start_idx:i+1]
                    try:
                        return json.loads(candidate)
                    except json.JSONDecodeError:
                        continue

    return None

def log_request_details(
    recording_id: Optional[str],
    json_template: List[Dict[str, Any]],
    token_usage: Optional[TokenUsage],
    timing_info: Optional[TimingInfo]
):
    """Append request details to an NDJSON log file (one JSON object per line)."""
    try:
        if len(json_template) == 7:
            template_type = "Kiran"
        elif len(json_template) == 13:
            template_type = "Urmila"
        else:
            template_type = "Unknown"

        utc_now = datetime.now(timezone.utc)
        india_now = utc_now.astimezone(ZoneInfo("Asia/Kolkata"))

        log_entry = {
            "recording_id": recording_id,
            "template": template_type,
            "utc_datetime": utc_now.isoformat(),
            "date": india_now.strftime("%Y-%m-%d"),
            "time": india_now.strftime("%H:%M:%S"),
            "token_usage": token_usage.dict() if token_usage else None,
            "timing_info": timing_info.dict() if timing_info else None
        }

        log_path = Path(DETAILS_LOG_PATH)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        logger.info(f"Logged request details for recording_id: {recording_id}")
    except Exception as e:
        logger.error(f"Error logging request details: {e}")


def save_test_files(recording_id: str, prompt: str, raw_response: str, extracted_json: Dict[str, Any]):
    """
    Save test files for debugging purposes.
    Creates a folder with the recording_id and saves three files:
    1. input.txt - contains the prompt
    2. raw_output.json - contains the raw response from vLLM
    3. processed_output.json - contains the extracted JSON
    """
    try:
        test_dir = Path(f"test_outputs/{recording_id}")
        test_dir.mkdir(parents=True, exist_ok=True)
        
        with open(test_dir / "input.txt", "w", encoding="utf-8") as f:
            f.write(prompt)
        
        with open(test_dir / "raw_output.json", "w", encoding="utf-8") as f:
            json.dump({"response": raw_response}, f, indent=2, ensure_ascii=False)
        
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

@app.post("/generate", response_model=MedicalNoteResponse)
async def generate_medical_note(
    request: MedicalNoteRequest,
    authorization: Optional[str] = Header(None, description="Bearer token for vLLM API authentication")
):
    """
    Generate a structured medical note from a transcript using Qwen 30B A3B Instruct.
    Requires Authorization header with Bearer token for vLLM access.
    """
    # Check if API key is provided
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="API key required. Use Authorization: Bearer <your_vllm_api_key>"
        )
    
    # Extract the API key from the header
    api_key = authorization.replace("Bearer ", "").strip()
    
    total_start_time = time.time()
    
    try:
        # Format transcript
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
        
        # Call vLLM server with API key authentication
        generation_start_time = time.time()
        
        payload = {
            "model": MODEL,
            "messages": messages,
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "max_tokens": MAX_TOKENS,
            "frequency_penalty": FREQUENCY_PENALTY,
            "presence_penalty": PRESENCE_PENALTY,
            "stream": False
        }
        
        # Add API key to request headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        response = requests.post(VLLM_API_URL, json=payload, headers=headers, timeout=300)
        response.raise_for_status()
        
        vllm_response = response.json()
        generation_time_ms = (time.time() - generation_start_time) * 1000
        
        # Extract content from vLLM response
        if "response" in vllm_response:
            content = vllm_response["response"]
        else:
            # Fallback: OpenAI-style response with choices
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
        
        processing_time_start = time.time()
        extracted_json = extract_json_from_response(content)
        processing_time_ms = (time.time() - processing_time_start) * 1000
        
        # Calculate total time
        total_time_ms = (time.time() - total_start_time) * 1000
        
        # Save test files if recording_id is provided
        if request.recording_id:
            save_test_files(request.recording_id, prompt, content, extracted_json or {})
        
        timing_info = TimingInfo(
            total_time_ms=total_time_ms,
            generation_time_ms=generation_time_ms,
            processing_time_ms=processing_time_ms
        )
        
        result = MedicalNoteResponse(
            success=True,
            generated_json=extracted_json,
            token_usage=token_usage,
            timing=timing_info
        )

        if request.recording_id:
            try:
                test_dir = Path(f"test_outputs/{request.recording_id}")
                test_dir.mkdir(parents=True, exist_ok=True)
                with open(test_dir / "final_response.json", "w", encoding="utf-8") as f:
                    json.dump(result.dict(), f, indent=2, ensure_ascii=False)
                logger.info(f"Saved final response for recording_id: {request.recording_id}")
                log_request_details(request.recording_id, request.json_template, token_usage, timing_info)

            except Exception as e:
                logger.error(f"Error saving final response: {e}")   

        return result
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            logger.error("Invalid API key provided to vLLM")
            return MedicalNoteResponse(
                success=False,
                error_message="Invalid API key. Please check your vLLM API key."
            )
        logger.error(f"HTTP error from vLLM: {e}")
        return MedicalNoteResponse(
            success=False,
            error_message=f"vLLM server error: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error generating medical note: {e}")
        return MedicalNoteResponse(
            success=False,
            error_message=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)