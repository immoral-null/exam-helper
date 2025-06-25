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
SUPPORTED_EXTS = {".png", ".jpg", ".jpeg"}

# Optional configuration
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
