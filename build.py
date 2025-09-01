import PyInstaller.__main__
import unidic

dicdir = unidic.DICDIR
dst = "unidic_data"
sep = ";"

PyInstaller.__main__.run([
    "main.py",
    "--name=KotobaTray",
    "--onedir",
    "--windowed",
    "--noconfirm",
    "--icon=tray-icon.ico",
    f"--add-data=NotoSerifJP-VariableFont_wght.ttf{sep}fonts",
    f"--add-data={dicdir}{sep}{dst}",
])
