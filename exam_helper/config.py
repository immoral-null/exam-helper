import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # only loads .env if it exists

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
	print("❌ OPENAI_API_KEY is not set. Please set it in your environment or .env file.")
	sys.exit(1)

INPUT_FOLDER = Path("data/screenshots")
OUTPUT_FOLDER = Path("data/answers")
SUPPORTED_EXTS = {".png", ".jpg", ".jpeg"}
