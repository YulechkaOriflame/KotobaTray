# KotobaTray

A small desktop utility built with **PySide6** that helps with Japanese learning:  
- Displaying stickers with custom vocabulary (stickers).  
- Translating text automatically from the clipboard. You need only to copy text.  
- On-the-fly translations with copy-back support.  

It lives in the system tray, and you can toggle windows on/off at any time.

---

## 🔧 Installation (Dev)
Developed and tested with **Python 3.13**

You don’t need to set up Python manually — just run the provided installer script.  
It will:
- Create a virtual environment in `.venv`
- Install dependencies from `requirements.txt`
- Download the **UniDic** dictionary for Japanese parsing

```bash
python install.py
```

After the script finishes, everything is ready to use.

---

## 🚀 Usage
When the app is running, a tray icon will appear.
From the tray menu you can open or close the available windows, and access basic options.

- Options - Switch between languages
- Clear clipboard (also cleared automatically on startup)
- Pause clipboard monitoring

### Windows
- Sticker Window — shows vocabulary from your CSV file for quick recall / learning
- Detailed Translation — clipboard monitoring, Japanese is always the source language
- Simple Translation — clipboard monitoring with simpler output
- Translate To — type text and see the translation in real time.
Clicking on the translation copies it back to the clipboard.
---

## 📦 Tech Stack
- PySide6 — UI framework  
- unidic — dictionary for Japanese parsing  
- Custom helpers (based on Qt framework) for clipboard monitoring, translation, and text formatting  

---

# 📝 Notes
- Works on Windows, macOS, and Linux (where PySide6 is supported).
- Uses Google Translate by default