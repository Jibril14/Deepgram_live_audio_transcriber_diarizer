import os
import requests
from dotenv import load_dotenv

load_dotenv(".env")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

audio_file_path = "sample.wav"

# Deepgram API endpoint with diarization enabled
url = "https://api.deepgram.com/v1/listen?diarize=true"

with open(audio_file_path, "rb") as audio_file:
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "audio/wav"
    }

    print("Uploading audio to Deepgram...")
    response = requests.post(url, headers=headers, data=audio_file)

if response.status_code == 200:
    result = response.json()
    print("Transcription & Diarization Result:")
    print("Res", result)
else:
    print(f"Error {response.status_code}: {response.text}")
