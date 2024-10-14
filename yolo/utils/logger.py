import logging

from rich.console import Console
from rich.logging import RichHandler

logger = logging.getLogger("YOLO_logger")
logger.setLevel(logging.DEBUG)
logger.propagate = False
if not logger.hasHandlers():
    logger.addHandler(RichHandler(console=Console(), show_level=True, show_path=True, show_time=True))