import os
import sys
from pathlib import Path

def init_unidic():
    if hasattr(sys, "_MEIPASS"):  # exe
        base = Path(sys._MEIPASS)
    else:  # dev
        base = Path(__file__).resolve().parent
    dic_path = base / "unidic"
    os.environ["UNIDICDIR"] = str(dic_path)

init_unidic()

from app import app

if __name__ == "__main__":
    app.init()
