import os
import time
import requests

# --- Настройки ---
API_KEY = "bmlrYS50YXF0YXFpc2h2aWxpLjFAYnR1LmVkdS5nZQ:oyWHcZETdtgqN2peijfXy"  # clientKey:secret
SOURCE_URL = "https://d-id-public-bucket.s3.us-west-2.amazonaws.com/alice.jpg"
SCRIPT_TEXT = "Making videos is easy with D-ID"

# Папка для сохранения видео
VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

# --- Создание talk ---
create_url = "https://api.d-id.com/talks"
payload = {
    "source_url": SOURCE_URL,
    "script": {
        "type": "text",
        "input": "I appreciate you asking! Yes. The International Relations Office at BTU offers exchange opportunities for students at all levels. Programs include Erasmus+ (funded by the European Commission) and bilateral partnerships. Students can participate in short- and long-term exchanges, as well as summer and winter schools, with full or partial funding.",
        "provider": {
            "type": "microsoft",
            "voice_id": "en-US-Emma2:DragonHDLatestNeural"
        }

    },
    "presenter_id": "v2_public_Amber@0zSz8kflCN"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Basic {API_KEY}"   # <-- заменили Bearer на Basic
}

response = requests.post(create_url, json=payload, headers=headers)
data = response.json()
print("Ответ при создании:", data)

talk_id = data.get("id")
if not talk_id:
    raise Exception(f"Не удалось создать talk: {data}")

print(f"Talk создан с ID: {talk_id}")

# --- Ожидание готовности ---
status_url = f"https://api.d-id.com/talks/{talk_id}"
status = ""
while status != "done":
    time.sleep(5)  # пауза между проверками
    r = requests.get(status_url, headers=headers)
    status_data = r.json()
    print("Ответ статуса:", status_data)
    status = status_data.get("status")

# --- Скачивание видео ---
video_url = status_data.get("result_url")
if video_url:
    video_response = requests.get(video_url)
    file_path = os.path.join(VIDEO_DIR, f"{talk_id}.mp4")
    with open(file_path, "wb") as f:
        f.write(video_response.content)
    print(f"Видео сохранено: {file_path}")
else:
    print("Видео ещё не готово или произошла ошибка.")
