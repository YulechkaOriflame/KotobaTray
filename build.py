import PyInstaller.__main__

PyInstaller.__main__.run([
    "main.py",
    "--name=KotobaTray",
    "--onedir",
    "--windowed",
    "--noconfirm",
    "--icon=tray-icon.png",
    "--add-data=NotoSerifJP-VariableFont_wght.ttf;fonts",
    "--add-data=unidic;unidic",
])