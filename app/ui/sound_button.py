import os
import tempfile
import threading
import time

import pygame
from PySide6.QtWidgets import QPushButton
from gtts import gTTS

from app.ui.random_button import RandomButton


class SpeakButton:
    def __init__(self, random_button: RandomButton):
        self.random_button = random_button
        self.button = QPushButton("🔊")
        self.button.setStyleSheet("""
            QPushButton {
                border: none;
                background: transparent;
                font-size: 16px;
            }
            QPushButton:hover {
                color: #0078d7;
            }
        """)
        self.button.clicked.connect(self._on_click)

    def _on_click(self):
        speak(self.random_button.words[self.random_button.index].text)


def speak(text: str, lang: str = "ja"):
    def _play():
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tmp_path = tmp_file.name
                gTTS(text=text, lang=lang).save(tmp_path)

            if not pygame.mixer.get_init():
                pygame.mixer.init()

            pygame.mixer.music.load(tmp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            time.sleep(0.1)  # Небольшая задержка для надёжности
            os.remove(tmp_path)

        except Exception as e:
            print("Ошибка озвучки:", e)

    threading.Thread(target=_play, daemon=True).start()
