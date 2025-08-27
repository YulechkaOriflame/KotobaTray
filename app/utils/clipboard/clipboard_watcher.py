from PySide6.QtCore import QObject, QTimer
from PySide6.QtWidgets import QApplication

class ClipboardWatcher(QObject):
    def __init__(self, callback, interval=200, parent=None):
        """
        :param callback: function to be called when the text in the buffer changes
        callback(text: str)
        :param interval: buffer check interval in milliseconds
        :param parent: parent QObject
        """
        super().__init__(parent)
        self._callback = callback
        self._interval = interval
        self._clipboard = QApplication.clipboard()
        self._last_text = ""
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._check_clipboard)

    def start(self):
        self._timer.start(self._interval)

    def stop(self):
        self._timer.stop()

    def _check_clipboard(self):
        text = self._clipboard.text()
        if text != self._last_text:
            self._last_text = text
            self._callback(text)
