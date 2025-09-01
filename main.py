import os
import sys
from pathlib import Path

def init_unidic():
    base = Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else Path(__file__).resolve().parent
    dic_path = base / "unidic"
    os.environ["UNIDICDIR"] = str(dic_path)

init_unidic()

from app import app

if __name__ == "__main__":
    app.init()
