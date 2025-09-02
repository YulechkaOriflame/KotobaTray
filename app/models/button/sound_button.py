import os
import tempfile
import threading
import time
from typing import Optional

import pygame
from gtts import gTTS
from PySide6.QtWidgets import QPushButton

from app.utils.catch_error_from_thread import error_call

class SoundButton(QPushButton):
    def __init__(self):
        super().__init__("🔊")
        self._text = ""
        self._lang = "ja"
        self.setStyleSheet(self._style())
        self.clicked.connect(self._on_click)

    def set_text(self, text: str, language: Optional[str] = "ja"):
        self._text = text
        self._lang = language

    def _on_click(self):
        speak(self._text, self._lang)

    @staticmethod
    def _style() -> str:
        return """
            QPushButton {
                border: none;
                background: transparent;
                font-size: 16px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
        """

def speak(text: str, lang: str):
    threading.Thread(target=_play_worker, args=(text, lang), daemon=True).start()

def _play_worker(text: str, lang: str):
    try:
        tmp_path = _generate_audio(text, lang)
        _play_audio(tmp_path)
        _cleanup(tmp_path)
    except Exception as e:
        error_call.error_signal.emit(str(e))

def _play_audio(file_path: str):
    _init_mixer()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

def _cleanup(file_path: str):
    time.sleep(0.1)
    try:
        os.remove(file_path)
    except OSError as e:
        error_call.error_signal.emit(str(e))

def _generate_audio(text: str, lang: str = "ja") -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name
    gTTS(text=text, lang=lang).save(tmp_path)
    return tmp_path

def _init_mixer():
    if not pygame.mixer.get_init():
        pygame.mixer.init()
