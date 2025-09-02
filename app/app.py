from PySide6.QtWidgets import QApplication

from app.tray import Tray

def init():
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)
    tray = Tray()
    tray.show()
    app.exec()
