import music21 as m21
from . import circle5ths, scales, get_enharmonic

m21_scales = {'Major': m21.scale.MajorScale,
              'Minor': m21.scale.MinorScale, 'Melodic Minor': m21.scale.MelodicMinorScale,
              'Harmonic Minor': m21.scale.HarmonicMinorScale,
              'Chromatic': m21.scale.ChromaticScale,
              'Dorian': m21.scale.DorianScale,
              'Hypoaeolian': m21.scale.HypoaeolianScale,
              'Hypodorian': m21.scale.HypodorianScale,
              'Hypophrygian': m21.scale.HypophrygianScale,
              'Hypolydian': m21.scale.HypolydianScale,
              'Hypomixolydian': m21.scale.HypomixolydianScale,
              'Hypolocrian': m21.scale.HypolocrianScale,
              'Lydian': m21.scale.LydianScale,
              'Locrian': m21.scale.LocrianScale,
              'Mixolydian': m21.scale.MixolydianScale,
              'Octatonic': m21.scale.OctatonicScale,
              'Phrygian': m21.scale.PhrygianScale,
              'RagAsawari': m21.scale.RagAsawari,
              'RagMarwa': m21.scale.RagMarwa,
              'Weighted Hexatonic Blues': m21.scale.WeightedHexatonicBlues,
              'Whole Tone': m21.scale.WholeToneScale
              }


class Scale:
    def __init__(self, tonic: str, acc: str = '', mode: str = 'Major'):
        """
        Instantiates a Scale object
        Args:
            tonic: Tonic or Root of the scale
            acc: accidental if any of the root
            mode: scale mode name.
        """
        assert (mode in scales) or (mode in m21_scales)
        assert acc in ['#', '-', '']
        self.tonic = tonic + acc
        self.mode = mode

    def get_notes(self) -> list[str]:
        """
        Returns list of scale notes
        """
        if self.mode in m21_scales:
            return [p.name for p in m21_scales[self.mode](self.tonic).pitches]
        hscale = m21.scale.ChromaticScale(self.tonic)
        return [hscale.pitches[j].name for j in scales[self.mode]]

    @property
    def stream(self):
        """
        Scale as a music21 Stream Object for saving
        """
        return m21.stream.Stream([m21.note.Note(p) for p in self.get_notes()])
