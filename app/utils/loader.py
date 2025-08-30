import csv
import os
from pathlib import Path
from typing import List

from PySide6.QtWidgets import QMessageBox

from entity.word_entry import WordEntry

def load_words(path: str) -> List[WordEntry]:
    try:
        with open(path, encoding="utf-8") as f:
            return [WordEntry(*r) for r in csv.reader(f) if len(r) == 4]
    except (OSError, csv.Error) as e:
        QMessageBox.information(
            None,
            "File not loaded",
            f"Error: {e}"
        )
        return []

def get_file(file_name: str) -> str:
    path = Path(__file__).parents[2] / file_name
    return str(path).replace('/', os.sep)
