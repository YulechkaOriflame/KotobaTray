import random

class RandomOrder:
    def __init__(self, size: int):
        self.size = size
        self.indices = list(range(size))
        self.pointer = 0
        self._shuffle()

    def _shuffle(self):
        random.shuffle(self.indices)

    def _reset(self):
        self._shuffle()
        self.pointer = 0

    def next(self) -> int:
        if self.pointer == self.size:
            self._reset()
        result = self.indices[self.pointer]
        self.pointer += 1
        return result
