import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # only loads .env if it exists

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
	print("❌ GEMINI_API_KEY is not set. Please set it in your environment or .env file.")
	sys.exit(1)

INPUT_FOLDER = Path("data/screenshots")
OUTPUT_FOLDER_ANSWERS = Path("data/answers")
OUTPUT_FOLDER_SUMMARY = Path("data/summary")
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg"}

# Optional configuration
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

PROMPT = os.getenv("PROMPT")
if PROMPT is None:
	PROMPT = (
		"Read the exam question in the image carefully.\n"
		"\n"
		"Return:\n"
		"- The question number (if visible).\n"
		"- The question text.\n"
		"- Any visible answer options.\n"
		"\n"
		"Then:\n"
		"- If the image shows answer options that are meant to be chosen from (e.g., multiple choice), "
		"rate each answer with a confidence score as a percentage (00–99%).\n"
		"- If no answer options are present, and the question requires a written answer, provide a short, "
		"direct answer in the same language and formatting as the image.\n"
		"- If the question is informational and does not ask for an answer, just return the content without adding anything.\n"
		"\n"
		"Rules:\n"
		"- Do NOT explain, translate, or rephrase.\n"
		"- Do NOT make up any content.\n"
		"- Keep the output faithful to the original language, numbering, and layout.\n"
		"\n"
		"Format:\n"
		"## <Question number>\n"
		"<Question text>\n"
		"\n"
		"If answer options are present:\n"
		"- <2-digit confidence>%: <Answer A>\n"
		"- <2-digit confidence>%: <Answer B>\n"
		"...\n"
		"\n"
		"If no answer options but a direct answer is expected:\n"
		"- Answer: <your answer here>"
	)


# Convert to logging level (or fallback to INFO if invalid)
LOG_LEVEL = getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO)