import os
import sys

import fugashi
import jaconv
import unidic_lite
from deep_translator import GoogleTranslator

def get_dicdir():
    if hasattr(sys, "_MEIPASS"):
        path = os.path.join(sys._MEIPASS, "unidic_lite", "dicdir")
    else:
        path = unidic_lite.DICDIR
    return os.path.abspath(path)

dicdir = get_dicdir()
print("Using dicdir:", dicdir)
print("dicrc exists:", os.path.exists(os.path.join(dicdir, "dicrc")))

tagger = fugashi.Tagger(f'-r {os.devnull} -d "{dicdir}"')

def get_underlined_text(text: str) -> str:
    words = [word.surface for word in tagger(text)]
    return "&#8201;".join(f"<u>{w}</u>" for w in words)

def get_romaji(text: str) -> str:
    tokens = tagger(text)
    romaji_words = []
    for token in tokens:
        reading = token.feature.kana if token.feature.kana else token.surface
        romaji_words.append(jaconv.kata2alphabet(reading))
    return " ".join(romaji_words)

def get_translation_from_source(text: str, source: str, target: str) -> str:
    return GoogleTranslator(source=source, target=target).translate(text)

def get_translation_to_target(text: str, source: str, target: str) -> str:
    return GoogleTranslator(source=source, target=target).translate(text)
