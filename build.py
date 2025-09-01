import PyInstaller.__main__
import unidic

PyInstaller.__main__.run([
    "main.py",
    "--name=KotobaTray",
    "--onedir",
    "--windowed",
    "--noconfirm",
    "--icon=tray-icon.ico",
    "--add-data=NotoSerifJP-VariableFont_wght.ttf;fonts",
    f"--add-data={unidic.DICDIR};unidic"
])
