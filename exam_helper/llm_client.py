from pathlib import Path

import google.generativeai as genai

from exam_helper.config import GEMINI_API_KEY, GEMINI_MODEL, PROMPT
from exam_helper.logger import setup_logger

logger = setup_logger()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)


def ask_chatgpt(image_path: Path) -> str:
    with image_path.open("rb") as f:
        img_bytes = f.read()

    response = None
    try:
        response = model.generate_content(
            contents=[PROMPT, {"mime_type": "image/png", "data": img_bytes}]
        )

        candidates = response.candidates
        if candidates and candidates[0].content.parts:
            return candidates[0].content.parts[0].text.strip()

        logger.error(f"❌ Empty response or no valid parts. Full response:\n{response}")
        return "[No valid answer returned]"

    except Exception as e:
        logger.error(f"❌ Error processing response. Error is:\n{e}\nresponse is:\n{response}")
        return "[Error processing response]"
