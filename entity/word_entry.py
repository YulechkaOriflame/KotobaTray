from dataclasses import dataclass


@dataclass
class WordEntry:
    text: str
    furigana: str
    romaji: str
    translation: str