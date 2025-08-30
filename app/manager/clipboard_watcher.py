from typing import Callable, List

from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtWidgets import QApplication

class ClipboardWatcher(QObject):
    changed = Signal(str)

    def __init__(self, interval=200):
        super().__init__()
        self._callbacks: List[Callable[[str], None]] = []
        self._interval = interval
        self._clipboard = QApplication.clipboard()
        self._last_text = ""
        self._clipboard.clear()
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._check_clipboard)

    def configure(self, callback: Callable[[str], None], parent: QObject) -> "ClipboardWatcher":
        self.setParent(parent)
        if callback not in self._callbacks:
            self._callbacks.append(callback)
        return self

    def start(self):
        self._timer.start(self._interval)

    def pause(self):
        self._timer.stop()

    def resume(self):
        self._timer.start(self._interval)

    def clear(self):
        self._last_text = ""
        self._clipboard.clear()
        self.changed.emit("")

    def _check_clipboard(self):
        text = self._clipboard.text()
        if text != self._last_text:
            self._last_text = text
            for cb in self._callbacks:
                cb(text)
            self.changed.emit(text)
