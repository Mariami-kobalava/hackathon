import requests
import time
from app.core.config import D_ID_API_KEY

D_ID_URL = "https://api.d-id.com/talks"  # D-ID endpoint

def generate_avatar_response(avatar_name: str, text: str):
    headers = {
        "Authorization": f"Bearer {D_ID_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "source": {"type": "image_url", "image_url": f"https://myserver.com/avatars/{avatar_name}.png"},
        "script": {"type": "text", "input": text},
        "voice": {"type": "female", "voice_id": "alloy"}
    }

    response = requests.post(D_ID_URL, json=data, headers=headers)
    result = response.json()

    # If we got a job ID, poll for completion
    if 'id' in result:
        job_id = result['id']
        return poll_for_video(job_id)

    return result

def poll_for_video(job_id: str, max_attempts: int = 30):
    """Poll D-ID API until video is ready"""
    headers = {
        "Authorization": f"Bearer {D_ID_API_KEY}"
    }

    for attempt in range(max_attempts):
        response = requests.get(f"{D_ID_URL}/{job_id}", headers=headers)
        result = response.json()

        if result.get('status') == 'done':
            return {
                'status': 'done',
                'video_url': result.get('result_url'),
                'job_id': job_id
            }
        elif result.get('status') == 'error':
            return {
                'status': 'error',
                'error': result.get('error', 'Unknown error'),
                'job_id': job_id
            }

        time.sleep(2)  # Wait 2 seconds before next poll

    return {
        'status': 'timeout',
        'job_id': job_id
    }
