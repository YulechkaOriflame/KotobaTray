# word-sticker (jp -> any lang)

Небольшая утилита, которая отображает слово в маленьком полупрозрачном окне, всегда поверх других окон.  
Позволяет переключать слова и озвучивать их (через `gTTS` и `pygame`).
> ⚠️ Программа не содержит словаря, его нужно подгружать отдельно при запуске.

## 📄 Формат CSV-файла

Пример `words.csv`:
- 日本,にほん,nihon,Япония

# Запуск
### Из кода
> python bu.py -f words.csv (words.csv - заменить на ваш путь к файлу)

### Так же можно собрать в 1 файл
> python -m zipapp Word-sticker -o sticker.pyz -m "bu:main"

### И запускать как
> python sticker.pyz -f Word-sticker/words.csv (Word-sticker/words.csv - путь до csv)

Выход
>q + Enter в терминал

Оффтоп коммент:
Дареному коду в зубы не смотрят :)

# Word Sticker

A small utility that shows a floating, always-on-top window with a word sticker.  
You can switch between words and have them spoken out loud (using `gTTS` and `pygame`).
> ⚠️ The program does **not** include any built-in dictionary — you must load your own CSV file at startup.

## 📄 CSV Format

Example `words.csv`:
- 日本,にほん,nihon,Japan

You can use your own columns, just make sure it matches the expected format
## 🚀 Running

### From source:
> python bu.py -f words.csv

### Bundled into a single file:
> python -m zipapp Word-sticker -o sticker.pyz -m "bu:main"

### Then run:
> python sticker.pyz -f Word-sticker/words.csv

❌ Exit
Type q + Enter in the terminal.

