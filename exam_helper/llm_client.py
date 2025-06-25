from pathlib import Path

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from exam_helper.config import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)


def ask_chatgpt(image_path: Path) -> str:
    with image_path.open("rb") as f:
        img_bytes = f.read()

    prompt = "Answer this exam question clearly and briefly. Use the same language as in the question."

    response = model.generate_content(
        [prompt, {"mime_type": "image/png", "data": img_bytes}],
        generation_config=GenerationConfig(max_output_tokens=500)
    )

    return response.text.strip()
