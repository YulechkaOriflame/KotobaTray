from typing import List

from PySide6.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout

from app.models.button.sound_button import SoundButton
from app.models.window.base_window import BaseWindow
from app.utils.clipboard.clipboard_watcher import ClipboardWatcher
from app.utils.label_builder import adjust_size, get_jp_label, get_label
from app.utils.translate.translate_and_format import get_romaji, get_translation_from_jp, get_underlined_text

LABEL_SCHEMAS = [
    (get_jp_label, 24),   # kanji
    (get_label, 20),      # romaji
    (get_label, 20),      # translation
]

class TranslationWindow(BaseWindow):
    def setup_window(self):
        ClipboardWatcher(self._on_clipboard_change, parent=self).start()
        self._build_layout()

    def _build_layout(self):
        main_layout = QVBoxLayout()
        self._add_labels(main_layout)
        self._add_sound_button(main_layout)
        self.setLayout(main_layout)

    def _add_labels(self, main_layout):
        self.labels = self._create_labels()
        for lbl in self.labels:
            main_layout.addWidget(lbl)

    def _add_sound_button(self, main_layout):
        self.sound_button = SoundButton()
        h_layout = QHBoxLayout()
        h_layout.addStretch()  # empty space from left
        h_layout.addWidget(self.sound_button)
        main_layout.addLayout(h_layout)

    def _on_clipboard_change(self, text: str):
        self.sound_button.set_text(text)
        self.labels[0].setText(get_underlined_text(text))
        self.labels[1].setText(get_romaji(text))
        self.labels[2].setText(get_translation_from_jp(text))
        self.adjustSize()

    @staticmethod
    def _create_labels() -> List[QLabel]:
        labels = [fn(size) for fn, size in LABEL_SCHEMAS]
        adjust_size(labels)
        return labels
