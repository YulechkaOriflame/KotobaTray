# translate_to_window.py
from PySide6.QtGui import QShowEvent
from PySide6.QtWidgets import QTextEdit, QVBoxLayout

from app.models.window.base_window import BaseWindow
from app.models.window.options_window import Options
from app.utils.copy_helper import CopyHelper
from app.manager.translator_manager import TranslatorManager

class TranslateToWindow(BaseWindow):
    def __init__(self, options: Options):
        self.translator = TranslatorManager(options)
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self._add_layout()
        self._add_input_field()
        self._add_copy_field()
        self.translator.translated.connect(self._update_copy_field)

    def _add_layout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def _add_input_field(self):
        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Write text here...")
        self.layout.addWidget(self.input_field)
        self.input_field.textChanged.connect(self._on_text_changed)

    def _on_text_changed(self):
        self.translator.translate(self.input_field.toPlainText())

    def _add_copy_field(self):
        self.copy_field = QTextEdit()
        self.copy_field.setReadOnly(True)
        self.copy_field.setStyleSheet("background-color: #eee;")
        CopyHelper.enable_copy(self.copy_field)
        self.layout.addWidget(self.copy_field)

    def _update_copy_field(self, text):
        self.copy_field.setText(text)

    def showEvent(self, event: QShowEvent) -> None:
        super().showEvent(event)
        # This method is called after the window is hidden to, if necessary,
        # pull up the current settings before showing
