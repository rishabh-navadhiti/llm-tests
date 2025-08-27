import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor
import traceback

rec_ids = [
    6645, 6642, 6639, 6635, 6632, 6627, 6625, 6622, 6614, 6613,
    6610, 6608, 6607, 6605, 6604, 6602, 6881, 6883, 6895, 6897, 6904,
    6911, 6922, 7051, 7060, 7062, 7067, 7074, 7079, 7092, 7284, 7270,
    7262, 7241, 7220
]

BASE_URL = "https://api.physicianassist.com/api/v1"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImlkIjoiNjdhMmY2NDY0YWRjZmU0NDBlOGJlNzUxIiwiZW1haWwiOiJ0ZWNoc3VwcG9ydEBwaHlzaWNpYW5hc3Npc3QuY29tIiwicHJvdmlkZXIiOiJtaWNyb3NvZnQiLCJvcmlnaW4iOiJQT1JUQUwifSwiZXhwIjoxNzU2MjEyNDY2fQ.GK7Pn888S_MjLutl27yiMF__lS27Cne9DptsSJT_KJc"
DEVICE_ID = "68ad9ee3936420a5438e21d3"

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "authorization": AUTH_TOKEN,
    "deviceid": DEVICE_ID,
    "ngrok-skip-browser-warning": "true",
    "origin": "https://portal.physicianassist.com",
    "referer": "https://portal.physicianassist.com/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}


def safe_request(method, url, **kwargs):
    """Make a safe HTTP request with error handling"""
    try:
        if method.upper() == 'GET':
            response = requests.get(url, timeout=30, **kwargs)
        elif method.upper() == 'POST':
            response = requests.post(url, timeout=30, **kwargs)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        print(f"Request to {url}: Status {response.status_code}")
        
        # Check if request was successful
        if response.status_code not in [200, 201]:
            print(f"ERROR: HTTP {response.status_code} - {response.text}")
            return None
        
        return response.json()
    
    except requests.exceptions.Timeout:
        print(f"ERROR: Request timeout for {url}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"ERROR: Connection error for {url}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Request exception for {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON response from {url}: {e}")
        print(f"Response text: {response.text[:500]}...")
        return None
    except Exception as e:
        print(f"ERROR: Unexpected error for {url}: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return None


def fetch_doctor_notes(note_id):
    """Step 2: Fetch doctor note details"""
    print(f"Fetching doctor notes for note ID: {note_id}")
    url = f"{BASE_URL}/doctor_notes/{note_id}"
    payload = {"data": {"fields_to_return": []}}
    
    return safe_request('POST', url, 
                       headers={**HEADERS, "content-type": "application/json"}, 
                       json=payload)


def fetch_transcription(transcription_id):
    """Step 3: Fetch transcription details"""
    print(f"Fetching transcription for transcription ID: {transcription_id}")
    url = f"{BASE_URL}/transcriptions"
    payload = {"data": {"transcription_id": transcription_id}}
    
    return safe_request('POST', url, 
                       headers={**HEADERS, "content-type": "application/json"}, 
                       json=payload)


def safe_file_write(file_path, data):
    """Safely write data to file with error handling"""
    try:
        # Check if directory exists and is writable
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            print(f"Directory {directory} does not exist, creating...")
            os.makedirs(directory, exist_ok=True)
        
        if not os.access(directory, os.W_OK):
            print(f"ERROR: No write permission for directory: {directory}")
            return False
        
        # Write the file
        with open(file_path, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        # Verify file was written
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            print(f"✓ Successfully saved to {file_path} ({os.path.getsize(file_path)} bytes)")
            return True
        else:
            print(f"ERROR: File {file_path} was not created or is empty")
            return False
            
    except PermissionError as e:
        print(f"ERROR: Permission denied writing to {file_path}: {e}")
        return False
    except OSError as e:
        print(f"ERROR: OS error writing to {file_path}: {e}")
        return False
    except Exception as e:
        print(f"ERROR: Unexpected error writing to {file_path}: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return False

# ... keep all your imports, rec_ids, BASE_URL, HEADERS etc. the same ...

def fetch_notes_and_transcripts(rec_ids):
    print(f"Starting processing of {len(rec_ids)} record IDs...")
    print(f"Current working directory: {os.getcwd()}")

    success_count = 0
    error_count = 0

    for i, rec_id in enumerate(rec_ids, 1):
        print(f"\n{'='*50}")
        print(f"Processing record ID: {rec_id} ({i}/{len(rec_ids)})")
        print(f"{'='*50}")

        try:
            # Step 1: Get doctor notes by recording
            url1 = f"{BASE_URL}/doctor_notes/rec/{rec_id}"
            data1 = safe_request('GET', url1, headers=HEADERS)

            if data1 is None or "result" not in data1 or "Notes" not in data1["result"]:
                print(f"ERROR: Invalid response for {rec_id}")
                error_count += 1
                continue

            note_id = data1["result"]["Notes"]["doctor_notes_versions"][0]
            transcription_id = data1["result"]["Notes"].get("transcription_id")

            if not note_id or not transcription_id:
                print(f"ERROR: Missing IDs for {rec_id}")
                error_count += 1
                continue

            print(f"Found note_id: {note_id}, transcription_id: {transcription_id}")

            # Run Step 2 and Step 3 concurrently
            with ThreadPoolExecutor(max_workers=2) as executor:
                future_notes = executor.submit(fetch_doctor_notes, note_id)
                future_transcript = executor.submit(fetch_transcription, transcription_id)
                notes = future_notes.result()
                transcript = future_transcript.result()

            if notes is None or transcript is None:
                print(f"ERROR: Failed fetching data for {rec_id}")
                error_count += 1
                continue

            # Extract values
            try:
                note_text = notes['result']['Notes']['notes']
            except Exception as e:
                print(f"ERROR: Cannot extract note text for {rec_id}: {e}")
                error_count += 1
                continue

            try:
                transcript_text = transcript['result']['Transcriptions']['dialogue_conversation']
            except Exception as e:
                print(f"ERROR: Cannot extract transcript text for {rec_id}: {e}")
                error_count += 1
                continue

            # ⚡ Save the extracted JSONs directly
            note_path = os.path.join("benchmark-gemini", f"REC-{rec_id}.json")
            transcript_path = os.path.join("transcripts", f"REC-{rec_id}.json")

            os.makedirs("benchmark-gemini", exist_ok=True)
            os.makedirs("transcripts", exist_ok=True)

            with open(note_path, "w", encoding="utf-8") as f:
                f.write(note_text if isinstance(note_text, str) else json.dumps(note_text, indent=4, ensure_ascii=False))

            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(transcript_text if isinstance(transcript_text, str) else json.dumps(transcript_text, indent=4, ensure_ascii=False))

            print(f"✓ Successfully processed {rec_id}")
            success_count += 1

        except Exception as e:
            print(f"ERROR: Unexpected error processing {rec_id}: {e}")
            print(traceback.format_exc())
            error_count += 1

    print(f"\n{'='*50}")
    print(f"SUMMARY: {success_count} successful, {error_count} errors")
    print(f"{'='*50}")


if __name__ == "__main__":
    fetch_notes_and_transcripts(rec_ids)
    print("Processing completed.")
