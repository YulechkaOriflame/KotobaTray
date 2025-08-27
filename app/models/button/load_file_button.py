from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFileDialog, QMessageBox, QPushButton

from app.utils.loader import load_words

class LoadFileButton(QPushButton):
    wordsLoaded = Signal(list)

    def __init__(self):
        super().__init__("📂")
        self.setToolTip("Load CSV file")
        self.setStyleSheet(self._style())
        self.clicked.connect(self._open_file)

    def _open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose CSV", "",
            "CSV files (*.csv);;All files (*)"
        )

        if file_path:
            words = load_words(file_path)
            self.wordsLoaded.emit(words)
            QMessageBox.information(self, "File loaded", f"Loaded words: {len(words)}")

    @staticmethod
    def _style() -> str:
        return """
            QPushButton {
                border: none;
                background: transparent;
                font-size: 16px;
            }
        """
