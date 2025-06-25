from pathlib import Path

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from exam_helper.config import GEMINI_API_KEY, GEMINI_MODEL, RESPONSE_LANG

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)


def ask_chatgpt(image_path: Path) -> str:
    with image_path.open("rb") as f:
        img_bytes = f.read()

    prompt_map = {
        "de": "Beantworte diese Prüfungsfrage auf Deutsch und so klar und knapp wie möglich.",
        "en": "Answer this exam question clearly and briefly.",
    }
    prompt = prompt_map.get(RESPONSE_LANG, prompt_map["en"])

    response = model.generate_content(
        [prompt, {"mime_type": "image/png", "data": img_bytes}],
        generation_config=GenerationConfig(max_output_tokens=500)
    )

    return response.text.strip()
