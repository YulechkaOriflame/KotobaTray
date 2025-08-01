from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtWidgets import QWidget, QLabel
import os


# noinspection PyUnresolvedReferences
class _DraggableWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._mouse_pos = None
        self.setWindowOpacity(0.7)
        self.setStyleSheet("""
            QWidget {
                background-color: #fdf6e3;
            }
        """)
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint
        )

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


def get_window() -> QWidget:
    return _DraggableWindow()


# noinspection PyUnresolvedReferences
def get_jp_label(size: int) -> QLabel:
    font_id = QFontDatabase.addApplicationFont(_get_jp_font())
    family = QFontDatabase.applicationFontFamilies(font_id)[0]
    label = QLabel()
    label.setFont(QFont(family, size))
    label.setAlignment(Qt.AlignCenter)
    return label


# noinspection PyUnresolvedReferences
def get_label(size: int) -> QLabel:
    label = QLabel()
    label.setFont(QFont("Comic Sans MS", size))
    label.setAlignment(Qt.AlignCenter)
    return label


def _get_jp_font() -> str:
    path = Path(__file__).parents[2] / "entity" / "NotoSerifJP-VariableFont_wght.ttf"
    return str(path).replace('/', os.sep)