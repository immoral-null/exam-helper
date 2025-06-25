from pathlib import Path

from watchdog.events import FileSystemEventHandler

from exam_helper.config import OUTPUT_FOLDER_ANSWERS, OUTPUT_FOLDER_SUMMARY, SUPPORTED_EXTS
from exam_helper.llm_client import ask_chatgpt
from exam_helper.logger import setup_logger

logger = setup_logger()


class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file = Path(event.src_path)
        if file.suffix.lower() in SUPPORTED_EXTS:
            logger.info(f"📸 New screenshot: {file.name}")
            try:
                answer = ask_chatgpt(file)
                self._save_answer(file, answer)
                self._append_to_summary(file.name, answer)
            except Exception as e:
                logger.error(f"❌ Error processing {file.name}: {e}")

    @staticmethod
    def _save_answer(file: Path, answer: str):
        out_file = OUTPUT_FOLDER_ANSWERS / f"{file.stem}.txt"
        with out_file.open("w", encoding="utf-8") as f:
            f.write(answer)
        logger.info(f"✅ Answer saved: {out_file}")

    @staticmethod
    def _append_to_summary(filename: str, answer: str):
        summary_path = OUTPUT_FOLDER_SUMMARY / "summary.txt"
        with summary_path.open("a", encoding="utf-8") as summary:
            summary.write(f"{filename} =\n")
            for line in answer.strip().splitlines():
                summary.write(f"    {line}\n")
            summary.write("\n")
