from PySide6.QtCore import QObject, QTimer, Signal

from app.models.window.options_window import Options
from app.manager.translator_thread import TranslatorThread

class TranslatorManager(QObject):
    translated = Signal(str)

    def __init__(self, options: Options, delay=1000):
        super().__init__()
        self._delay = delay
        self._timer = QTimer(self)
        self._options = options
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._start_translation)

        self._pending_text = ""
        self._current_thread: TranslatorThread | None = None

    def translate(self, text: str):
        self._pending_text = text
        self._timer.start(self._delay)

    def _start_translation(self):
        text = self._pending_text.strip()
        if not text:
            self.translated.emit("")
            return

        if self._current_thread and self._current_thread.isRunning():
            return

        thread = TranslatorThread(text, self._options)
        thread.translated.connect(self.translated.emit)
        thread.finished.connect(self._clear_thread)

        self._current_thread = thread
        self._current_thread.start()

    def _clear_thread(self):
        if self._current_thread:
            self._current_thread.deleteLater()
            self._current_thread = None
