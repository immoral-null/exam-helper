import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from exam_helper.config import INPUT_FOLDER, OUTPUT_FOLDER, SUPPORTED_EXTS
from exam_helper.gpt_client import ask_chatgpt
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
                out_file = OUTPUT_FOLDER / f"{file.stem}.txt"
                with out_file.open("w", encoding="utf-8") as f:
                    f.write(answer)
                logger.info(f"✅ Answer saved: {out_file}")
            except Exception as e:
                logger.error(f"❌ Error processing {file.name}: {e}")


def start_monitoring():
    INPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, str(INPUT_FOLDER), recursive=False)
    observer.start()
    logger.info(f"📂 Watching folder: {INPUT_FOLDER}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
