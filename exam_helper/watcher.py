import os
import time

from watchdog.observers import Observer

from exam_helper.config import INPUT_FOLDER, OUTPUT_FOLDER_ANSWERS, OUTPUT_FOLDER_SUMMARY
from exam_helper.logger import setup_logger
from exam_helper.screenshot_handler import ScreenshotHandler

logger = setup_logger()


def wait_for_file_complete(path, timeout=5, interval=0.5):
    """Wait until file size stops changing."""
    deadline = time.time() + timeout
    last_size = -1
    while time.time() < deadline:
        try:
            current_size = os.path.getsize(path)
            if current_size == last_size:
                return True
            last_size = current_size
        except FileNotFoundError:
            pass
        time.sleep(interval)
    return False


class DelayedScreenshotHandler(ScreenshotHandler):
    def on_created(self, event):
        if not event.is_directory:
            if wait_for_file_complete(event.src_path):
                super().on_created(event)
            else:
                logger.warning(f"⚠️ File not stable: {event.src_path}")


def start_monitoring():
    INPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    OUTPUT_FOLDER_ANSWERS.mkdir(parents=True, exist_ok=True)
    OUTPUT_FOLDER_SUMMARY.mkdir(parents=True, exist_ok=True)

    event_handler = DelayedScreenshotHandler()
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
