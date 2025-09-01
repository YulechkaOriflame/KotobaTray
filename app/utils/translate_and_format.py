import fugashi
import jaconv
from deep_translator import GoogleTranslator

tagger = fugashi.Tagger()

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
