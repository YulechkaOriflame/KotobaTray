from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._mouse_pos = None
        self.setWindowOpacity(0.7)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setStyleSheet(self._style())
        self.setup_window()

    @abstractmethod
    def setup_window(self):
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._mouse_pos is not None and event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._mouse_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self._mouse_pos = None

    @staticmethod
    def _style() -> str:
        return """
            QWidget {
                background-color: #fdf6e3;
            }
            QLineEdit, QTextEdit {
                font-size: 16px;
                padding: 5px;
            }
        """
