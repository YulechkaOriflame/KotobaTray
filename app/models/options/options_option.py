from PySide6.QtGui import QAction
from PySide6.QtWidgets import QSystemTrayIcon, QWidget

class OptionsOption(QAction):
    def __init__(self, window: QWidget, parent: QSystemTrayIcon):
        super().__init__("Options", parent)
        self.options_window = window
        self.triggered.connect(self._toggle_options)

    def _toggle_options(self):
        if self.options_window.isVisible():
            self.options_window.hide()
        else:
            self.options_window.show()
            self.options_window.raise_()
            self.options_window.activateWindow()
