from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt


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
def get_label(size: int) -> QLabel:
    label = QLabel()
    label.setFont(QFont("Comic Sans MS", size))
    label.setAlignment(Qt.AlignCenter)
    return label