import math


class Euclid:
    """Euclidean Rhythm generator"""

    def __init__(self, notes: int, length: int):
        self.notes = notes
        self.length = length
        self.rhythm = self._bjorklund()

    def _bjorklund(self) -> list:
        """
        Bjorklunds algorithm to generate the Euclidean rhythm
        Returns:
        """
        seq = [[1] if i < self.notes else [0] for i in range(self.length)]
        for n, i in enumerate(range(self.notes, self.length)):
            if seq[n] == [1]:
                seq[n].extend(seq[i])
        seq = seq[:n + 1]
        remainder = sum([len(j) < len(seq[0]) for j in seq])
        while remainder > 1:
            l = len(seq[0])
            i = 0
            for s in seq:
                if len(s) < l:
                    seq[i].extend(s)
                    i += 1
            seq = seq[:-i]
            remainder = sum([len(j) < len(seq[0]) for j in seq])
        rh = []
        for el in seq:
            rh += el
        return rh

    def __repr__(self) -> str:
        return ''.join(['X' if n else '.' for n in self.rhythm])
