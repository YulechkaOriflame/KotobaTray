from typing import List

from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout

from app.models.button.load_file_button import LoadFileButton
from app.models.button.random_button import RandomButton
from app.models.button.sound_button import SoundButton
from app.models.window.base_window import BaseWindow
from app.utils.label_builder import get_jp_label, get_label

class StickerWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setLayout(self._build_layout())

    def _build_layout(self) -> QVBoxLayout:
        main_layout = QVBoxLayout()
        labels = self._create_labels()
        self._set_layout_for_labels(main_layout, labels)
        self._add_buttons(main_layout, labels)
        return main_layout

    def _add_buttons(self, main_layout: QVBoxLayout, labels: List[QLabel]):
        button_row = QHBoxLayout()
        load_file_button = LoadFileButton()
        sound_button = SoundButton()
        random_button = RandomButton(self, labels, load_file_button, sound_button)

        for btn in (random_button, sound_button, load_file_button):
            button_row.addWidget(btn)
        main_layout.addLayout(button_row)

    @staticmethod
    def _set_layout_for_labels(main_layout: QVBoxLayout, labels: List[QLabel]):
        for lbl in labels:
            main_layout.addWidget(lbl)

    @staticmethod
    def _create_labels() -> List[QLabel]:
        kanji_label = get_jp_label(40)
        furigana_label = get_jp_label(28)
        romaji_label = get_label(14)
        translation_label = get_label(16)
        return [kanji_label, furigana_label, romaji_label, translation_label]
