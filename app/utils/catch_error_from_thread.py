from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

class GuiHelper(QObject):
    error_signal = Signal(str)
    """Catch error from threads and show it in main"""

    def __init__(self):
        super().__init__()
        self.error_signal.connect(self._show_error)

    @staticmethod
    def _show_error(message: str):
        QMessageBox.information(None, "Error", message)

error_call = GuiHelper()
