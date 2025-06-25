import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv
from google.generativeai.types import GenerationConfig

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")


def ask_chatgpt(image_path: Path) -> str:
    with image_path.open("rb") as f:
        img_bytes = f.read()

    prompt = "Answer this exam question clearly and briefly."

    response = model.generate_content(
        [prompt, {"mime_type": "image/png", "data": img_bytes}],
        generation_config=GenerationConfig(max_output_tokens=500)
    )

    return response.text.strip()
