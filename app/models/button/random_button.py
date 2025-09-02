from PySide6.QtWidgets import QLabel, QPushButton, QWidget

from app.models.button.load_file_button import LoadFileButton
from app.models.button.sound_button import SoundButton
from app.utils.random import RandomOrder
from entity.word_entry import WordEntry

class RandomButton(QPushButton):
    def __init__(self,
                 window: QWidget,
                 labels: list[QLabel],
                 loader: LoadFileButton,
                 sound: SoundButton
                 ):
        super().__init__("Next")
        self.setStyleSheet(self._style())
        self._window_state(window, labels)
        self._random_state()
        self.sound = sound
        self.clicked.connect(self._on_random)
        loader.wordsLoaded.connect(self._on_words_loaded)

    def _window_state(self, window, labels):
        self.window = window
        self.labels = labels

    def _random_state(self):
        self.index = 0
        self.words = []
        self.order: RandomOrder | None = None

    def _on_random(self):
        i = self.order.next()
        self.update_labels(i)

    def _resize_window(self):
        self.window.adjustSize()
        self.window.setFixedSize(self.window.size())

    def update_labels(self, i):
        self.sound.set_text(self.words[i].text)
        self.labels[0].setText(self.words[i].text)
        self.labels[1].setText(self.words[i].furigana)
        self.labels[2].setText(self.words[i].romaji)
        self.labels[3].setText(self.words[i].translation)
        self._resize_window()

    def _on_words_loaded(self, words: list[WordEntry]):
        self.words = words
        self.order = RandomOrder(len(words))
        if words:
            self.update_labels(0)

    @staticmethod
    def _style() -> str:
        return """
            QPushButton {
                background-color: #eee8d5;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 4px 10px;
            }
            QPushButton:hover {
                background-color: #e0dacb;
            }
            QPushButton:pressed {
                background-color: #d6cfbf;
                padding-left: 12px;
                padding-top: 6px;
            }
        """
