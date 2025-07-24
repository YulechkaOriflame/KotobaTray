import sys
import threading
from typing import List

from PySide6.QtWidgets import QHBoxLayout, QApplication, QVBoxLayout, QLabel

from app.ui.random_button import RandomButton
from app.ui.sound_button import speak, SpeakButton
from app.ui.window_props import get_window, get_label
from entity.word_entry import WordEntry

app = QApplication(sys.argv)

def _create_labels() -> list[QLabel]:
    return [get_label(size) for size in [40, 28, 16, 16]]

def _add_widgets(layout: QVBoxLayout, widgets: list):
    for w in widgets:
        layout.addWidget(w)

def _listen_for_exit():
    print("q + Enter для завершения")
    for line in iter(input, ""):
        if line.strip().lower() == "q":
            QApplication.quit()
            break


def start_window(words: List[WordEntry]):
    window = get_window()
    layout = QVBoxLayout(window)
    labels = _create_labels()
    random_button = RandomButton(words, labels)
    sound_button = SpeakButton(random_button)
    
    _add_widgets(layout, labels)
    button_row = QHBoxLayout()
    button_row.addWidget(random_button.button)
    button_row.addWidget(sound_button.button)
    layout.addLayout(button_row)

    random_button.update_labels()
    window.show()
    threading.Thread(target=_listen_for_exit, daemon=True).start()
    app.exec()