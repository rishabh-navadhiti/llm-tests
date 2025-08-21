import os
import json
import logging
import time
from typing import Dict, Any, Optional
import google.generativeai as genai

# -------------------------------
# CONFIG
# -------------------------------
PROMPT_PATH = "eval_prompt.txt"
BENCHMARK_DIR = "benchmark"
CANDIDATE_DIR = "../Output/Deepseek-qwen32b-fp8-updatedTemp"
TRANSCRIPT_DIR = "../transcripts/Spencer"
OUTPUT_DIR = "/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_result/Eval-deepseek-qwen-gemini"
# PROMPT_PATH = "/Users/rish/Development/runpod dev/llm-tests/evaluation/eval_prompt.txt"
# BENCHMARK_DIR = "/Users/rish/Development/runpod dev/llm-tests/evaluation/testiing/bnch"
# CANDIDATE_DIR = "/Users/rish/Development/runpod dev/llm-tests/evaluation/testiing/op"
# TRANSCRIPT_DIR = "/Users/rish/Development/runpod dev/llm-tests/transcripts/Spencer"
# OUTPUT_DIR = "/Users/rish/Development/runpod dev/llm-tests/evaluation/testiing/eval"

MODEL_NAME = "gemini-2.5-flash"

# Logging configuration
LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# -------------------------------
# SETUP LOGGING
# -------------------------------
def setup_logging():
    """Setup comprehensive logging configuration."""
    # Create logs directory if it doesn't exist
    log_dir = os.path.join(OUTPUT_DIR, "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    # Setup file and console handlers
    log_file = os.path.join(log_dir, f"evaluation_{int(time.time())}.log")
    
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # Console output
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized. Log file: {log_file}")
    return logger

# -------------------------------
# SETUP GEMINI
# -------------------------------
def setup_gemini(logger: logging.Logger):
    """Setup Gemini API with error handling."""
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(MODEL_NAME)
        logger.info(f"Gemini model '{MODEL_NAME}' initialized successfully")
        return model
    except Exception as e:
        logger.error(f"Failed to setup Gemini: {e}")
        raise

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
def load_file(path: str, logger: logging.Logger) -> str:
    """Load text file with error handling."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        logger.debug(f"Successfully loaded file: {path} ({len(content)} chars)")
        return content
    except Exception as e:
        logger.error(f"Failed to load file {path}: {e}")
        raise

def load_json(path: str, logger: logging.Logger) -> Dict[str, Any]:
    """Load JSON file with error handling."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.debug(f"Successfully loaded JSON: {path}")
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {path}: {e}")
        raise
    except Exception as e:
        logger.error(f"Failed to load JSON file {path}: {e}")
        raise

def save_json(path: str, data: Dict[str, Any], logger: logging.Logger) -> None:
    """Save JSON file with error handling."""
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.debug(f"Successfully saved JSON: {path}")
    except Exception as e:
        logger.error(f"Failed to save JSON file {path}: {e}")
        raise

def find_candidate_file(record_id: str, logger: logging.Logger) -> Optional[str]:
    """Find candidate file with multiple naming options."""
    candidate_name_options = [
        f"{record_id}-output.processed.json",
        f"{record_id}-output.json",
        f"{record_id}.processed.json",
        f"{record_id}.json",
    ]
    
    logger.debug(f"Searching for candidate file for record_id: {record_id}")
    
    for option in candidate_name_options:
        path = os.path.join(CANDIDATE_DIR, option)
        if os.path.exists(path):
            logger.debug(f"Found candidate file: {path}")
            return path
        else:
            logger.debug(f"Candidate file not found: {path}")
    
    logger.warning(f"No candidate file found for {record_id}")
    return None

def find_transcript_file(record_id: str, logger: logging.Logger) -> Optional[str]:
    """Find transcript file for the given record_id."""
    transcript_path = os.path.join(TRANSCRIPT_DIR, f"{record_id}.json")
    
    if os.path.exists(transcript_path):
        logger.debug(f"Found transcript file: {transcript_path}")
        return transcript_path
    else:
        logger.warning(f"Transcript file not found: {transcript_path}")
        return None

def validate_json_response(response_text: str, logger: logging.Logger) -> Dict[str, Any]:
    """Validate and parse JSON response from Gemini."""
    try:
        # Clean up response text (remove markdown code blocks if present)
        cleaned_text = response_text.strip()
        if cleaned_text.startswith('```json'):
            cleaned_text = cleaned_text[7:]
        if cleaned_text.endswith('```'):
            cleaned_text = cleaned_text[:-3]
        cleaned_text = cleaned_text.strip()
        
        eval_result = json.loads(cleaned_text)
        logger.debug("Successfully parsed JSON response from Gemini")
        return eval_result
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON response: {e}")
        logger.error(f"Raw response: {response_text[:500]}...")
        raise

def call_gemini_with_retry(model, prompt: str, logger: logging.Logger, max_retries: int = 3) -> str:
    """Call Gemini API with retry logic."""
    for attempt in range(max_retries):
        try:
            logger.debug(f"Calling Gemini API (attempt {attempt + 1}/{max_retries})")
            response = model.generate_content(prompt)
            
            if not response.text:
                raise ValueError("Empty response from Gemini")
            
            logger.debug(f"Received response from Gemini ({len(response.text)} chars)")
            return response.text
            
        except Exception as e:
            logger.warning(f"Gemini API call failed (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt == max_retries - 1:
                logger.error(f"All Gemini API attempts failed for this request")
                raise
            time.sleep(2 ** attempt)  # Exponential backoff

# -------------------------------
# MAIN EVALUATION LOOP
# -------------------------------
def main():
    """Main evaluation function with comprehensive logging."""
    # Setup logging
    logger = setup_logging()
    
    # Track statistics
    stats = {
        'total_files': 0,
        'successful_evaluations': 0,
        'failed_evaluations': 0,
        'missing_candidates': 0,
        'missing_transcripts': 0,
        'start_time': time.time()
    }
    
    try:
        logger.info("Starting medical notes evaluation")
        logger.info(f"Configuration:")
        logger.info(f"  - Benchmark directory: {BENCHMARK_DIR}")
        logger.info(f"  - Candidate directory: {CANDIDATE_DIR}")
        logger.info(f"  - Transcript directory: {TRANSCRIPT_DIR}")
        logger.info(f"  - Output directory: {OUTPUT_DIR}")
        logger.info(f"  - Model: {MODEL_NAME}")
        
        # Ensure output directory exists
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        logger.info(f"Created output directory: {OUTPUT_DIR}")
        
        # Setup Gemini
        model = setup_gemini(logger)
        
        # Load the base evaluation prompt
        logger.info(f"Loading evaluation prompt from: {PROMPT_PATH}")
        base_prompt = load_file(PROMPT_PATH, logger)
        logger.info(f"Loaded prompt ({len(base_prompt)} characters)")
        
        # Get list of benchmark files
        benchmark_files = [f for f in os.listdir(BENCHMARK_DIR) if f.endswith(".json")]
        stats['total_files'] = len(benchmark_files)
        logger.info(f"Found {len(benchmark_files)} benchmark files to process")
        
        # Iterate over benchmark files
        for i, fname in enumerate(benchmark_files, 1):
            record_id = fname.replace(".json", "")
            logger.info(f"Processing {i}/{len(benchmark_files)}: {record_id}")
            
            try:
                # Load benchmark note
                benchmark_path = os.path.join(BENCHMARK_DIR, fname)
                logger.debug(f"Loading benchmark note: {benchmark_path}")
                benchmark_note = load_json(benchmark_path, logger)
                
                # Find and load transcript
                transcript_path = find_transcript_file(record_id, logger)
                transcript_note = None
                if transcript_path:
                    logger.debug(f"Loading transcript: {transcript_path}")
                    transcript_note = load_json(transcript_path, logger)
                else:
                    logger.warning(f"⚠️  No transcript found for {record_id}, continuing without it")
                    stats['missing_transcripts'] += 1
                
                # Find candidate file
                candidate_path = find_candidate_file(record_id, logger)
                if not candidate_path:
                    logger.warning(f"⚠️  Skipping {record_id}: No candidate file found")
                    stats['missing_candidates'] += 1
                    continue
                
                # Load candidate note
                logger.debug(f"Loading candidate note: {candidate_path}")
                candidate_note = load_json(candidate_path, logger)
                
                # Build prompt with transcript included
                logger.debug("Building evaluation prompt")
                prompt_parts = [base_prompt]
                
                if transcript_note:
                    prompt_parts.extend([
                        "\n\nTRANSCRIPT:",
                        json.dumps(transcript_note, indent=2)
                    ])
                
                prompt_parts.extend([
                    "\n\nBENCHMARK_NOTE:",
                    json.dumps(benchmark_note, indent=2),
                    "\n\nCANDIDATE_NOTE:",
                    json.dumps(candidate_note, indent=2)
                ])
                
                full_prompt = "".join(prompt_parts)
                logger.debug(f"Built prompt ({len(full_prompt)} characters)")
                
                # Call Gemini with retry logic
                response_text = call_gemini_with_retry(model, full_prompt, logger)
                
                # Parse and validate response
                eval_result = validate_json_response(response_text, logger)
                
                # Save result
                out_path = os.path.join(OUTPUT_DIR, f"{record_id}-eval.json")
                save_json(out_path, eval_result, logger)
                
                stats['successful_evaluations'] += 1
                logger.info(f"✅ Successfully evaluated {record_id} → {out_path}")
                
            except Exception as e:
                stats['failed_evaluations'] += 1
                logger.error(f"❌ Error evaluating {record_id}: {str(e)}", exc_info=True)
                
                # Save error information for debugging
                error_info = {
                    'record_id': record_id,
                    'error': str(e),
                    'timestamp': time.time()
                }
                error_path = os.path.join(OUTPUT_DIR, f"{record_id}-error.json")
                try:
                    save_json(error_path, error_info, logger)
                except:
                    logger.error(f"Failed to save error info for {record_id}")
        
        # Print final statistics
        elapsed_time = time.time() - stats['start_time']
        logger.info("=" * 50)
        logger.info("EVALUATION COMPLETE")
        logger.info("=" * 50)
        logger.info(f"Total files processed: {stats['total_files']}")
        logger.info(f"Successful evaluations: {stats['successful_evaluations']}")
        logger.info(f"Failed evaluations: {stats['failed_evaluations']}")
        logger.info(f"Missing candidates: {stats['missing_candidates']}")
        logger.info(f"Missing transcripts: {stats['missing_transcripts']}")
        logger.info(f"Success rate: {stats['successful_evaluations']/max(stats['total_files'], 1)*100:.1f}%")
        logger.info(f"Total time: {elapsed_time:.2f} seconds")
        logger.info(f"Average time per file: {elapsed_time/max(stats['total_files'], 1):.2f} seconds")
        
    except Exception as e:
        logger.error(f"Fatal error in main execution: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()