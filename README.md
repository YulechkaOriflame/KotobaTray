# KotobaTray

A small desktop utility built with **PySide6** that helps with Japanese learning:  
- Displaying stickers with custom vocabulary.  
- Translating text automatically from the clipboard.  
- On-the-fly translations with copy-back support.  

It lives in the system tray, and you can toggle windows on/off at any time.

---

## 🔧 Installation

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
From the tray, you can enable or disable any of the three windows:

```python
"Sticker": StickerWindow,
"Translate from": TranslationWindow,
"Translate to": TranslateToWindow,
```

### Sticker
Displays words from your custom CSV file.  
Useful for quick recall / learning.  

### Translate from
Monitors the clipboard and automatically shows translations of copied text.  

### Translate to
Lets you type text and see the translation in real time.  
Clicking on the translation copies it back into the clipboard.  

---

## 📦 Tech Stack
- PySide6 — UI framework  
- unidic-lite — dictionary for Japanese parsing  
- Custom helpers for clipboard monitoring, translation, and text formatting  

---

# 📝 Notes
- Works on Windows, macOS, and Linux (where PySide6 is supported).
- By default, translations are performed **Russian ↔ Japanese** using Google Translate.  
- You can change the source/target languages in `app/utils/translate/translate_and_format.py`.