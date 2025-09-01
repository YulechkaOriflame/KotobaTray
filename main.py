import os
import sys
from pathlib import Path

def init_unidic():
    base = Path(sys._MEIPASS) if hasattr(sys, "_MEIPASS") else Path(__file__).resolve().parent
    bundled = base / "unidic_data"
    if bundled.exists():
        os.environ["UNIDICDIR"] = str(bundled)
    else:
        try:
            import unidic
            os.environ.setdefault("UNIDICDIR", unidic.DICDIR)
        except Exception:
            pass

init_unidic()

from app import app

if __name__ == "__main__":
    app.init()
