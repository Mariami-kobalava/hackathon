import requests
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
    return response.json()  # დაბრუნდება JSON, სადაც URL არის ვიდეო ან ხმოვანი პასუხი
