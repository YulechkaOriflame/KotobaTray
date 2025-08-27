from PySide6.QtCore import QThread, Signal

from app.utils.translate.translate_and_format import get_translation_to_jp

class TranslatorThread(QThread):
    translated = Signal(str)

    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def run(self):
        self._translate_text()

    def _translate_text(self):
        result = get_translation_to_jp(self.text)
        self.translated.emit(result)

