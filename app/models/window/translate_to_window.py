# translate_to_window.py
from PySide6.QtWidgets import QLineEdit, QTextEdit, QVBoxLayout

from app.models.window.base_window import BaseWindow
from app.utils.clipboard.copy_helper import CopyHelper
from app.utils.translate.translator_manager import TranslatorManager

class TranslateToWindow(BaseWindow):
    def __init__(self):
        self.translator = TranslatorManager()
        super().__init__()

    def setup_window(self):
        self._add_layout()
        self._add_input_field()
        self._add_copy_field()
        self.translator.translated.connect(self._update_copy_field)

    def _add_layout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def _add_input_field(self):
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Write text here...")
        self.layout.addWidget(self.input_field)
        self.input_field.textChanged.connect(self._on_text_changed)

    def _on_text_changed(self):
        self.translator.translate(self.input_field.text())

    def _add_copy_field(self):
        self.copy_field = QTextEdit()
        self.copy_field.setReadOnly(True)
        self.copy_field.setStyleSheet("background-color: #eee;")
        CopyHelper.enable_copy(self.copy_field)
        self.layout.addWidget(self.copy_field)

    def _update_copy_field(self, text):
        self.copy_field.setText(text)
