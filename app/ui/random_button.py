import platform

from PySide6.QtWidgets import QPushButton, QLabel, QWidget

from app.utils import get_random_index
from entity.word_entry import WordEntry


class RandomButton:
    def __init__(
            self,
            words: list[WordEntry],
            window: QWidget,
            labels: list[QLabel]
    ):
        self.window = window
        self.index = 0
        self.button = QPushButton("Другое слово")
        self.words = words
        self.labels = labels
        self.button.clicked.connect(self._on_random)

    def _on_random(self):
        new_index = get_random_index(self.index, self.words)
        self.index = new_index
        self.update_labels()

    def _resize_window(self):
        self.window.adjustSize()
        self.window.setFixedSize(self.window.size())

    def update_labels(self):
        i = self.index
        self.labels[0].setText(self.words[i].text)
        self.labels[1].setText(self.words[i].furigana)
        self.labels[2].setText(self.words[i].romaji)
        self.labels[3].setText(self.words[i].translation)
        self._resize_window()
