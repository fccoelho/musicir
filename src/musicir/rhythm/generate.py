import math
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.collections import PatchCollection


class Euclid:
    """Euclidean Rhythm generator"""

    def __init__(self, notes: int, length: int):
        self.notes = notes
        self.length = length
        self.rhythm = self._bjorklund()

    def _bjorklund(self) -> list[int]:
        """
        Bjorklunds algorithm to generate the Euclidean rhythm
        Returns:
        """
        seq = [[1] if i < self.notes else [0] for i in range(self.length)]
        for n, i in enumerate(range(self.notes, self.length)):
            if seq[n] == [1]:
                seq[n].extend(seq[i])
        seq = seq[:-min(self.notes,(self.length-self.notes))]
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


class RhythmViewer:
    def __init__(self, rhythm):
        self.rhythm = rhythm
        self.polygon = self._polygon()

    def _polygon(self):
        cp = mp.CirclePolygon((0.5, 0.5), radius=.5, resolution=len(self.rhythm), fc='y')
        return cp

    def show(self):
        fig, ax = plt.subplots(figsize=(12, 12))
        patches = [self.polygon]
        verts = self.polygon.get_path().vertices[::-1]
        trans = self.polygon.get_patch_transform()
        points = trans.transform(verts)
        notes = []
        for n, pt in zip(self.rhythm, points):
            if n:
                note = plt.Circle(pt, radius=0.01, color='r')
                notes.append(pt)
                patches.append(note)
        notes += [notes[0]]

        collection = PatchCollection(patches, alpha=0.7)
        ax.add_collection(collection)
        ax.plot([p[0] for p in notes], [p[1] for p in notes], 'k')
        ax.axis('off')
