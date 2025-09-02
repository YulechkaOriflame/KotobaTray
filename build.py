import PyInstaller.__main__
import unidic_lite

PyInstaller.__main__.run([
    "main.py",
    "--name=KotobaTray",
    "--onefile",
    "--windowed",
    "--noconfirm",
    "--icon=tray-icon.ico",
    "--add-data=NotoSerifJP-VariableFont_wght.ttf;.",
    f"--add-data={unidic_lite.DICDIR};unidic_lite/dicdir",
])
