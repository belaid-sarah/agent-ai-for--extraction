import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Stocke ta clé dans .env

def call_gemini(prompt: str) -> str:
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY
    }
    
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"[Gemini Error] {response.status_code} - {response.text}")
    
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
