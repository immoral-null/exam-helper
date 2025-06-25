import time

from watchdog.observers import Observer

from exam_helper.config import INPUT_FOLDER, OUTPUT_FOLDER_ANSWERS, OUTPUT_FOLDER_SUMMARY
from exam_helper.logger import setup_logger
from exam_helper.screenshot_handler import ScreenshotHandler

logger = setup_logger()


def start_monitoring():
    INPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    OUTPUT_FOLDER_ANSWERS.mkdir(parents=True, exist_ok=True)
    OUTPUT_FOLDER_SUMMARY.mkdir(parents=True, exist_ok=True)

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
