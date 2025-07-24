from app.file_loader import load_words
from app.ui.app_window import start_window


def init():
    words = load_words()
    start_window(words)