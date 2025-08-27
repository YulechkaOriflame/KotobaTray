from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QTextEdit

class CopyHelper:
    @staticmethod
    def enable_copy(field: QTextEdit):
        field.mousePressEvent = lambda event: CopyHelper._copy_and_flash(field)

    @staticmethod
    def _copy_and_flash(field: QTextEdit):
        clipboard = QApplication.clipboard()
        clipboard.setText(field.toPlainText())
        original = field.styleSheet()
        field.setStyleSheet("background-color: #cfc;")
        QTimer.singleShot(200, lambda: field.setStyleSheet(original))
