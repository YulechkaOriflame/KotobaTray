import argparse
import csv
import sys
from typing import List

from entity.word_entry import WordEntry

parser = argparse.ArgumentParser(description="VApp — показ слов из CSV")
parser.add_argument("-f", "--file", required=True, help="Путь к файлу .csv")
args = parser.parse_args()


def load_words() -> List[WordEntry]:
    try:
        with open(args.file, encoding="utf-8") as f:
            return [WordEntry(*r) for r in csv.reader(f) if len(r) == 4]
    except (OSError, csv.Error) as e:
        sys.exit(f"Ошибка при чтении файла: {e}")
