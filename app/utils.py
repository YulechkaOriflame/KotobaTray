import random
from typing import List

from entity.word_entry import WordEntry


def get_random_index(current_index: int, list: List[WordEntry]) -> int:
    next_index = current_index
    while next_index == current_index:
        next_index = random.randint(0, len(list) - 1)
    return next_index
