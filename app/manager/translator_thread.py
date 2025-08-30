from PySide6.QtCore import QThread, Signal

from app.models.window.options_window import Options
from app.utils.translate_and_format import get_translation_to_target

class TranslatorThread(QThread):
    translated = Signal(str)

    def __init__(self, text: str, options: Options):
        super().__init__()
        self._options = options
        self.text = text

    def run(self):
        self._translate_text()

    def _translate_text(self):
        src, tgt = self._options.get_src(), self._options.get_tgt()
        result = get_translation_to_target(self.text, tgt, src)
        self.translated.emit(result)
