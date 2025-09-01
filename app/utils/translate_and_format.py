import os
import sys

import cutlet
import fugashi
from deep_translator import GoogleTranslator
from unidic import unidic

def make_tagger():
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
        dic_path = os.path.join(base_path, "unidic")
    else:
        dic_path = unidic.DICDIR

    return fugashi.Tagger(f'-d "{dic_path}"')
tagger = make_tagger()

def get_underlined_text(text: str) -> str:
    words = [word.surface for word in tagger(text)]
    return "&#8201;".join(f"<u>{w}</u>" for w in words)

def get_romaji(text: str) -> str:
    return cutlet.Cutlet().romaji(text)

def get_translation_from_source(text: str, source: str, target: str) -> str:
    return GoogleTranslator(source=source, target=target).translate(text)

def get_translation_to_target(text: str, source: str, target: str) -> str:
    return GoogleTranslator(source=source, target=target).translate(text)
