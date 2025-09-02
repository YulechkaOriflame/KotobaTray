import os
from pathlib import Path
from typing import List

from PySide6.QtGui import QFont, QFontDatabase, Qt
from PySide6.QtWidgets import QLabel

from app.utils.loader import get_file

# noinspection PyUnresolvedReferences
def get_jp_label(size: int) -> QLabel:
    font_id = QFontDatabase.addApplicationFont(get_jp_font())
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

def adjust_size(labels: List[QLabel]):
    for lbl in labels:
        lbl.setMaximumWidth(1000)
        lbl.setWordWrap(True)

def get_jp_font() -> str:
    return get_file("NotoSerifJP-VariableFont_wght.ttf")

