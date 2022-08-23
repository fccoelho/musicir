import math

import matplotlib.patches as mp
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from music21 import stream, instrument
from music21.note import Note, Rest
from music21.bar import Repeat


class Euclid:
    """Euclidean Rhythm generator"""

    def __init__(self, notes: int, length: int, start=1):
        self.notes = notes
        self.length = length
        self.start = start
        self.rhythm = self._bjorklund()
        self.get_beat()

    def _bjorklund(self) -> list[int]:
        """
        Bjorklunds algorithm to generate the Euclidean rhythm
        Returns:
        """
        seq = [[1] if i < self.notes else [0] for i in range(self.length)]
        for n, i in enumerate(range(self.notes, self.length)):
            if seq[n] == [1]:
                seq[n].extend(seq[i])
        seq = seq[: -min(self.notes, (self.length - self.notes))]
        remainder = sum(len(j) < len(seq[0]) for j in seq)
        while remainder > 1:
            l = len(seq[0])
            i = 0
            for s in seq[-remainder:]:
                if i == (len(seq) - remainder):
                    break
                seq[i].extend(s)
                i += 1
            seq = seq[:-i]
            remainder = sum(len(j) < len(seq[0]) for j in seq)
        rh = []
        for el in seq:
            rh += el
        return rh

    def __repr__(self) -> str:
        return "".join(["X" if n else "." for n in self.rhythm])

    def get_beat(self, times=2) -> stream.Stream:
        self.beat = stream.Stream()
        # self.beat.insert(0, instrument.Piano())
        meas = stream.Measure()
        meas.leftBarline = Repeat(direction='start')
        meas.rightBarline = Repeat(direction='end', times=times)

        n_idx = [i for i, n in enumerate(self.rhythm) if n]
        if self.start != 1:
            s_rhythm = self.rhythm[n_idx[self.start - 1]:] + self.rhythm[:n_idx[self.start - 1]]
        else:
            s_rhythm = self.rhythm
        for i in s_rhythm:
            if i == 1:
                n = Note("A4", type="eighth")
                meas.append(n)
            else:
                r = Rest(type='eighth')
                meas.append(r)
        self.beat.append(meas)
        return self.beat

    def play(self):
        self.beat.show('midi')


class RhythmViewer:
    # Visualization attributes
    radius = 0.5

    def __init__(self, rhythm):
        self.rhythm = rhythm
        self.polygon = self._polygon()

    def _polygon(self):
        cp = mp.CirclePolygon(
            (self.radius, self.radius), radius=self.radius, resolution=len(self.rhythm), fc="y"
        )
        return cp

    def show(self, circle: bool = True, lines: bool = True):
        """
        Plots rhythms on a circle.
        Args:
            circle: Draws the circle
            lines: Connect notes with lines
        """
        fig, ax = plt.subplots(figsize=(12, 12))
        patches = [self.polygon]
        if circle:
            patches.append(plt.Circle((self.radius, self.radius), radius=self.radius, color='k'))
        verts = self.polygon.get_path().vertices[::-1]
        trans = self.polygon.get_patch_transform()
        points = trans.transform(verts)
        notes = []
        for n, pt in zip(self.rhythm, points):
            if n:
                note = plt.Circle(pt, radius=0.01, color="r")
                notes.append(pt)
                patches.append(note)
        notes += [notes[0]]

        collection = PatchCollection(patches, alpha=0.7)
        ax.add_collection(collection)
        if lines:
            ax.plot([p[0] for p in notes], [p[1] for p in notes], "k")
        ax.axis("off")


traditional_rhythms = {
    'fandango': Euclid(4, 12),
    'cueca': Euclid(2, 3),
    'khafif-e-ramal': Euclid(2, 5),
    'cumbia': Euclid(3, 4),
    'calypso': Euclid(3, 4),
    'khalif-e-saghil': Euclid(3, 4),
    'khafif-e-ramal_2': Euclid(3, 5, 2),
    'ruchenitza': Euclid(3, 7),
    'tresillo': Euclid(3, 8),
    'ruchenitza_2': Euclid(4, 7),
    'aksak': Euclid(4, 9),
    'outside_now': Euclid(4, 11),
    'york-samai': Euclid(5, 6, 2),
    'Nawakhat': Euclid(5, 7),
    'cinquillo': Euclid(5, 8),
    'spanish_tango': Euclid(5, 8, 2),
    'al-saghil-al-sani': Euclid(5, 8, 2),
    'agsag-samai': Euclid(5, 9),
    'venda': Euclid(5, 9, 2),
    'pictures_at_an_exhibition': Euclid(5, 11),
    'venda_clapping': Euclid(5, 12),
    'bossa-nova': Euclid(5, 16, 3),
    'bendir': Euclid(7, 8),
    'mpre': Euclid(7, 12),
    'samba': Euclid(7, 16, 7),
    'agogo-samba': Euclid(9, 16, 4),
    'ngbaka-maibo': Euclid(9, 16, 8),
    'aka': Euclid(11, 24, 7),
    'aka_upper_sangha': Euclid(13, 24, 4)
}
