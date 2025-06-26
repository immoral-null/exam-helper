import logging

from exam_helper.config import LOG_LEVEL


def setup_logger():
    logger = logging.getLogger("exam_helper")
    if not logger.hasHandlers():
        logger.setLevel(LOG_LEVEL)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

def setup_writer():
    writer = logging.getLogger("exam_helper_writer")
    if not writer.hasHandlers():
        writer.setLevel(LOG_LEVEL)  # or logging.INFO
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(message)s"))  # << this line is key
        writer.addHandler(handler)
        writer.propagate = False
    return writer

