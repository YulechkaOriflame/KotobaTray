# translator_manager.py
from PySide6.QtCore import QObject, QTimer, Signal
from app.utils.translate.translator_thread import TranslatorThread

class TranslatorManager(QObject):
    translated = Signal(str)

    def __init__(self, delay=1000):
        super().__init__()
        self._delay = delay
        self._timer = QTimer()
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._start_translation)
        self._pending_text = ""
        self._current_thread: TranslatorThread | None = None

    def translate(self, text: str):
        self._pending_text = text
        self._timer.start(self._delay)

    def _start_translation(self):
        text = self._pending_text
        if not text.strip():
            self.translated.emit("")
            return

        if self._current_thread and self._current_thread.isRunning():
            self._current_thread.quit()
            self._current_thread.wait()

        self._current_thread = TranslatorThread(text)
        self._current_thread.translated.connect(self.translated.emit)
        self._current_thread.finished.connect(lambda: setattr(self, "_current_thread", None))
        self._current_thread.start()
