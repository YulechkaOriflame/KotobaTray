from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon

class QuitOption(QAction):
    def __init__(self, parent: QSystemTrayIcon):
        super().__init__("Quit", parent)
        self.triggered.connect(QApplication.instance().quit)
