import cutlet
import fugashi
from deep_translator import GoogleTranslator
tagger = fugashi.Tagger()

def get_underlined_text(text: str) -> str:
    words = [word.surface for word in tagger(text)]
    return "&#8201;".join(f"<u>{w}</u>" for w in words)

def get_romaji(text: str) -> str:
    return cutlet.Cutlet().romaji(text)

def get_translation_from_jp(text: str) -> str:
    return GoogleTranslator(source="ja", target="ru").translate(text)

def get_translation_to_jp(text: str) -> str:
    return GoogleTranslator(source="ru", target="ja").translate(text)
