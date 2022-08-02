import music21 as m21

circle5ths = (
    "C",
    "G",
    "D",
    "A",
    "E",
    "B | C-",
    "F# | G-",
    "C# | D-",
    "A-",
    "E-",
    "B-",
    "F",
)

notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

scales = {
    "Chromatic TriMirror": [0, 1, 2],
    "Do Re Mi": [0, 2, 4],
    "Flat 6 and 7": [0, 10, 11],
    "Major Flat 6": [0, 4, 8],
    "Major Triad 1": [0, 3, 8],
    "Major Triad 2": [0, 4, 7],
    "Major Triad 3": [0, 5, 9],
    "Messiaen 3rd Mode": [0, 4, 8],
    "Minor Triad 1": [0, 4, 9],
    "Minor Triad 2": [0, 3, 7],
    "Minor Triad 3": [0, 5, 8],
    "Minor TriChord": [0, 2, 3],
    "Phrygian TriChord": [0, 1, 3],
    "Sanagari 1": [0, 5, 10],
    "Sharp 6 and 7": [0, 10, 11],
    "Ute Tritone 1": [0, 3, 10],
    "Alternating TetraMirror 1": [0, 1, 3, 4],
    "Bi Yu": [0, 3, 7, 10],
    "Chromatic TetraMirror 1": [0, 1, 2, 3],
    "Diminished 7th Chord": [0, 3, 6, 9],
    "Dorian TetraChord": [0, 2, 3, 5],
    "Eskimo Tetratonic": [0, 2, 4, 7],
    "Genus Primum Inverse": [0, 5, 7, 10],
    "Har Minor TetraChord 1": [0, 2, 3, 6],
    "Major TetraChord 1": [0, 4, 7, 10],
    "Major TetraChord 2": [0, 4, 7, 11],
    "Major TetraChord 2": [0, 3, 8, 10],
    "Major TetraChord 3": [0, 2, 5, 10],
    "Major TetraChord 4": [0, 5, 7, 9],
    "Major TetraChord 5": [0, 4, 7, 10],
    "Major TetraChord 6": [0, 2, 6, 9],
    "Major TetraChord 7": [0, 3, 5, 9],
    "Major TetraChord 8": [0, 5, 7, 10],
    "Major TetraChord 9": [0, 3, 6, 8],
    "Major TetraChord 10": [0, 2, 5, 7],
    "Major TetraChord 11": [0, 2, 4, 5],
    "Sixth TetraChord 1": [0, 4, 7, 9],
    "Sixth TetraChord 2": [0, 2, 5, 9],
    "Sixth TetraChord 3": [0, 3, 6, 9],
    "Minor Seventh Chord": [0, 3, 7, 10],
    "Phrygian TetraChord": [0, 1, 3, 5],
    "Warao Minor TriChord": [0, 2, 3, 10],
    "Whole-Tone Tetramirror": [0, 2, 4, 6],
    "Sus 4 Pentatonic": [0, 2, 5, 7, 10],
    "M3 Mj Pentatonic": [0, 3, 5, 8, 10],
    "Chinese 6 Pentatonic": [0, 4, 6, 7, 11],
    "Han - kumoi": [0, 2, 5, 7, 8],
    "In": [0, 1, 5, 7, 8],
    "Yo": [0, 2, 5, 7, 9],
    "Indonesian 2 Pentatonic": [0, 1, 6, 7, 8],
    "Indonesian 3 Pentatonic": [0, 4, 5, 7, 11],
    "No Name": [0, 1, 4, 7, 9],
    "Altered Pentatonic": [0, 1, 5, 7, 9],
    "Balinese Pentachord 1": [0, 1, 4, 6, 7],
    "Blues #V": [0, 3, 5, 6, 11],
    "Blues Pentacluster 1": [0, 1, 2, 3, 6],
    "Blues PentaCluster 3": [0, 1, 2, 3, 5],
    "Blues PentaCluster 5": [0, 1, 2, 3],
    "Blues PentaCluster 6": [0, 1, 2, 3, 5],
    "Blues#V all flats": [0, 3, 5, 6, 11],
    "Center-Cluster PentaMirror": [0, 3, 4, 5, 8],
    "Chaio 1": [0, 2, 5, 8, 10],
    "Chromatic PentaMirror": [0, 1, 2, 3, 4],
    "Dominant Pentatonic": [0, 2, 4, 7, 10],
    "Slendro": [0, 2, 5, 7, 9],
    "Half Diminished plus b8": [0, 3, 6, 10, 11],
    "Japanese Pentachord 1": [0, 1, 3, 6, 7],
    "Kokin-Joshi": [0, 1, 5, 7, 10],
    "Kung": [0, 2, 4, 6, 9],
    "Locrian PentaMirror": [0, 1, 3, 5, 6],
    "Lydian Pentachord": [0, 2, 4, 6, 7],
    "Major Pentachord": [0, 2, 4, 5, 7],
    "Minor 6th Added": [0, 3, 5, 7, 9],
    "Minor Pentachord Chad G": [0, 2, 3, 5, 7],
    "Mixolydian Pentatonic 1": [0, 4, 5, 7, 10],
    "Oriental Pentacluster 1": [0, 1, 2, 5, 6],
    "Oriental Raga Guhamano": [0, 2, 5, 9, 10],
    "Romanian Bacovia 1": [0, 4, 5, 8, 11],
    "Spanish Pentacluster 1": [0, 1, 3, 4, 5],
    "Major Pentatonic": [0, 2, 4, 7, 9],
    "Minor Pentatonic": [0, 3, 5, 7, 10],
    "Pelog": [0, 1, 3, 7, 8],
    "Iwato": [0, 1, 5, 6, 10],
    "Kumoi Scale": [0, 2, 3, 7, 9],
    "Hirajoshi": [0, 2, 3, 7, 8],
    "Sus 4": [0, 2, 5, 7, 9, 10],
    "Augmented, Messiaen": [0, 3, 4, 7, 8, 11],
    "Blues Dorian Hexatonic 1": [0, 2, 3, 4, 7, 9],
    "Blues Dorian Hexatonic 2": [0, 1, 3, 4, 7, 9],
    "Blues Minor all flats": [0, 3, 5, 6, 7, 10],
    "Blues Minor Maj7": [0, 3, 5, 6, 7, 11],
    "Chromatic HexaMirror all #": [0, 1, 2, 3, 4, 5],
    "Chromatic HexaMirror all b": [0, 1, 2, 3, 4, 5],
    "Double-Phrygian Hexatonic": [0, 1, 3, 5, 6, 9],
    "Eskimo Hexatonic 1": [0, 2, 4, 6, 8, 9],
    "Eskimo Hexatonic 2": [0, 2, 4, 6, 8, 11],
    "Genus Secundum": [0, 4, 5, 7, 9, 11],
    "Hawaiian": [0, 2, 3, 7, 9, 11],
    "Honchoshi Plagal Form": [0, 1, 3, 5, 6, 10],
    "Lydian #2 Hexatonic": [0, 3, 4, 7, 9, 11],
    "Lydian b3 Hexatonic": [0, 3, 4, 7, 9, 11],
    "Lydian Hexatonic": [0, 2, 4, 7, 9, 11],
    "Major Bebop Hexatonic": [0, 2, 4, 7, 8, 9],
    "Major Blues alternate": [0, 2, 3, 4, 7, 9],
    "Minor Hexatonic": [0, 2, 3, 5, 7, 10],
    "Phrygian Hexatonic": [0, 3, 5, 7, 8, 10],
    "Prometheus 2": [0, 2, 4, 6, 9, 10],
    "Prometheus Neapolitan 2": [0, 1, 4, 6, 9, 10],
    "Pyramid Hexatonic": [0, 2, 3, 5, 6, 9],
    "Ritsu": [0, 1, 3, 5, 8, 10],
    "Scottish Hexatonic Arezzo": [0, 2, 4, 5, 7, 9],
    "Takemitsu Tree Line Mod 1": [0, 2, 3, 6, 8, 10],
    "Takemitsu Tree Line Mod 2": [0, 2, 3, 6, 8, 11],
    "Prometheus": [0, 2, 4, 6, 8, 10],
    "Prometheus Neopolitan": [0, 1, 4, 6, 8, 10],
    "Whole-tone": [0, 2, 4, 6, 8, 10],
    "Blues": [0, 3, 5, 6, 7, 10],
    "Sixtone Mode 1": [0, 3, 4, 7, 8, 11],
    "Sixtone Mode 2": [0, 1, 4, 5, 8, 9],
    "Ionian Augmented": [0, 2, 4, 5, 8, 9, 11],
    "Dorian #4": [0, 2, 3, 6, 7, 9, 10],
    "Mixolydian b9b13": [0, 1, 4, 5, 7, 8, 10],
    "Lydian #9": [0, 3, 4, 6, 7, 9, 11],
    "Alt Dominant bb7": [0, 1, 3, 4, 5, 8, 9],
    "Dorian b2": [0, 1, 3, 5, 7, 9, 10],
    "Lydian Aug": [0, 2, 4, 6, 8, 9, 11],
    "Lydian b7": [0, 2, 4, 6, 7, 9, 10],
    "Mixolydian b13": [0, 2, 4, 5, 7, 8, 10],
    "Locrian Nat 9": [0, 2, 3, 5, 6, 8, 10],
    "Alt Dominant": [0, 1, 3, 4, 6, 8, 10],
    "Locrian Nat 6": [0, 1, 3, 5, 6, 9, 10],
    "Hungarian Folk": [0, 1, 4, 5, 7, 8, 11],
    "Purvi": [0, 1, 4, 6, 7, 8, 11],
    "Todi": [0, 1, 3, 6, 7, 8, 11],
    "Saba": [0, 2, 3, 4, 7, 8, 10],
    "Spanish Dominant": [0, 1, 3, 6, 7, 8, 10],
    "Smyrneiko": [0, 2, 3, 6, 7, 9, 11],
    "Mixolydian b9": [0, 1, 4, 5, 7, 9, 10],
    "Major Locrian": [0, 2, 4, 5, 6, 8, 10],
    "Lydian Minor": [0, 2, 4, 6, 7, 8, 10],
    "Leading Wholetone": [0, 2, 4, 6, 8, 10, 11],
    "Oriental No1": [0, 1, 4, 5, 6, 8, 10],
    "Oriental No2": [0, 1, 4, 5, 6, 9, 10],
    "Neopolitan Major": [0, 1, 3, 5, 7, 9, 11],
    "Neopolitan Minor": [0, 1, 3, 5, 7, 8, 11],
    "Aeolian 2# 4# #5": [0, 3, 4, 6, 8, 9, 11],
    "Aeolian Flat 3b 5b 6b 8b": [0, 3, 4, 6, 8, 9, 11],
    "Aeolian Flat b3 b5 b6": [0, 3, 4, 6, 8, 9, 11],
    "Bhairubahar Thaat": [0, 1, 4, 5, 7, 9, 11],
    "Blues Heptatonic": [0, 3, 5, 6, 7, 9, 10],
    "Blues Modified": [0, 2, 3, 5, 6, 7, 10],
    "Blues Phrygian 1": [0, 1, 3, 5, 6, 7, 10],
    "Blues with Leading Tone": [0, 3, 5, 6, 7, 10, 11],
    "Chromatic Dorian": [0, 1, 2, 5, 7, 8, 9],
    "Chromatic Dorian Inverse": [0, 3, 4, 5, 7, 10, 11],
    "Chromatic HeptaMirror": [0, 1, 2, 3, 4, 5, 6],
    "Chromatic Hypodorian 1": [0, 2, 3, 4, 7, 8, 9],
    "Chromatic Hypodorian 2": [0, 2, 3, 4, 7, 8, 9],
    "Chromatic Hypodorian Inv": [0, 3, 4, 5, 8, 9, 10],
    "Chromatic Hypophrygian": [0, 1, 2, 5, 6, 7, 9],
    "Chromatic Lydian": [0, 1, 4, 5, 6, 9, 11],
    "Chromatic Mixolydian 1": [0, 1, 2, 4, 6, 7, 10],
    "Chromatic Mixolydian 2": [0, 1, 2, 5, 6, 7, 10],
    "Chromatic Mixolydian Inv": [0, 2, 5, 6, 7, 10, 11],
    "Chromatic Phrygian": [0, 3, 4, 5, 8, 10, 11],
    "Chromatic Phrygian Inverse": [0, 1, 2, 4, 7, 8, 9],
    "Dorian b5": [0, 2, 3, 5, 6, 9, 10],
    "Enigmatic Ascending 1": [0, 1, 4, 6, 8, 10, 11],
    "Enigmatic Descending 1": [0, 1, 4, 5, 8, 10, 11],
    "Enigmatic Minor": [0, 1, 3, 6, 8, 10, 11],
    "Enigmatic Minor all #s": [0, 1, 3, 6, 8, 10, 11],
    "Enigmatic Minor all bs": [0, 1, 3, 6, 8, 10, 11],
    "Pelog alternate": [0, 4, 6, 7, 8, 11],
    "Gipsy Hexatonic 1": [0, 1, 5, 6, 8, 9, 10],
    "Gypsy Hexatonic 5": [0, 1, 4, 5, 7, 8, 9],
    "Hindi 5 flats": [0, 1, 3, 4, 6, 8, 10],
    "Houzam": [0, 3, 4, 5, 7, 9, 11],
    "Hungarian Gypsy 1": [0, 2, 3, 6, 7, 8, 10],
    "Phrygian dim 4th": [0, 1, 3, 4, 7, 8, 10],
    "Phrygian dim 4th alternate": [0, 1, 3, 4, 7, 8, 10],
    "Jazz Minor Inverse": [0, 1, 3, 5, 7, 9, 10],
    "Locrian 2": [0, 2, 3, 5, 6, 8, 11],
    "Locrian bb7": [0, 1, 3, 5, 6, 8, 9],
    "Lydian Augmented 2": [0, 1, 3, 4, 6, 8, 10],
    "Marva or Marvi": [0, 1, 4, 6, 7, 9, 11],
    "Marva Thaat": [0, 1, 4, 6, 7, 9, 11],
    "Major Bebop Heptatonic": [0, 2, 4, 5, 7, 8, 9],
    "Minor Bebop 1": [0, 2, 3, 4, 7, 9, 10],
    "Minor Bebop Heptatonic": [0, 2, 3, 4, 7, 9, 10],
    "Mixolydian Augmented": [0, 2, 4, 5, 8, 9, 10],
    "Mixolydian b5": [0, 2, 4, 5, 6, 9, 10],
    "Neapolitan Minor Mode": [0, 1, 2, 4, 6, 8, 9],
    "Nohkan 1": [0, 2, 5, 6, 8, 9, 11],
    "Nohkan 2": [0, 2, 5, 6, 8, 9, 11],
    "Rock n Roll 1": [0, 3, 4, 5, 7, 9, 10],
    "Rock n Roll 2": [0, 3, 4, 5, 7, 9, 10],
    "Romanian Major": [0, 1, 4, 6, 7, 9, 10],
    "Sabach 1": [0, 2, 3, 4, 7, 8, 10],
    "Sabach 2": [0, 2, 3, 4, 7, 8, 10],
    "Spanish Heptatonic 1": [0, 3, 4, 5, 6, 8, 10],
    "Spanish Heptatonic 2": [0, 3, 4, 5, 6, 8, 10],
    "Super Locrian all sharps": [0, 1, 3, 4, 6, 8, 10],
    "Superlocrian, Diminished 1": [0, 1, 3, 4, 6, 8, 10],
    "Superlocrian, Diminished 2": [0, 1, 3, 4, 6, 8, 10],
    "Todi b7 1": [0, 1, 3, 6, 7, 9, 10],
    "Todi b7 2": [0, 1, 3, 6, 7, 9, 10],
    "Ultra Locrian 1": [0, 1, 3, 4, 6, 8, 9],
    "Ultra Locrian 2": [0, 1, 3, 4, 6, 8, 9],
    "Major": [0, 2, 4, 5, 7, 9, 11],
    "Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Lydian": [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "Minor": [0, 2, 3, 5, 7, 8, 10],
    "Locrian": [0, 1, 3, 5, 6, 8, 10],
    "Harmonic Minor": [0, 2, 3, 5, 7, 8, 11],
    "Harmonic Major": [0, 2, 4, 5, 7, 8, 11],
    "Melodic Minor": [0, 2, 3, 5, 7, 9, 11],
    "Hungarian Gypsy 1": [0, 2, 3, 6, 7, 8, 11],
    "Hungarian Gypsy 2": [0, 2, 3, 6, 7, 8, 10],
    "Hungarian Major": [0, 3, 4, 6, 7, 9, 10],
    "Enigmatic": [0, 1, 4, 6, 8, 10, 11],
    "Persian": [0, 1, 4, 5, 6, 8, 11],
    "Composite Blues": [0, 3, 4, 5, 6, 7, 10],
    "Dorian Bebop": [0, 2, 3, 4, 5, 7, 9, 11],
    "Adonai Malakh 1": [0, 1, 2, 3, 5, 7, 9, 10],
    "Adonai Malakh 2": [0, 1, 2, 3, 5, 7, 9, 10],
    "Algerian": [0, 2, 3, 5, 6, 7, 8, 11],
    "Auxillary Diminished": [0, 2, 3, 5, 6, 8, 9, 11],
    "Blues Diminished": [0, 1, 3, 4, 6, 7, 9, 10],
    "Blues Octatonic": [0, 2, 3, 5, 6, 7, 9, 10],
    "Chromatic OctaMirror": [0, 1, 2, 3, 4, 5, 6, 7],
    "Diminished": [0, 2, 3, 5, 6, 8, 9, 11],
    "Dorian Aeolian 1": [0, 2, 3, 5, 7, 8, 9, 10],
    "Dorian Aoelian 2": [0, 2, 3, 5, 7, 8, 9, 10],
    "Enigmatic alternate 1": [0, 1, 4, 5, 6, 8, 10, 11],
    "Enigmatic alterate 2": [0, 1, 4, 5, 6, 8, 10, 11],
    "Half-Dimiished Bebop": [0, 1, 3, 5, 6, 7, 8, 11],
    "Half-Diminished Symmetrrical": [0, 1, 3, 4, 6, 7, 9, 10],
    "Harmonic Neapolitan Minor 1": [0, 1, 2, 3, 5, 7, 8, 11],
    "Harmonic Neapolitan Minor 2": [0, 1, 2, 3, 5, 7, 8, 11],
    "Harmonic Neapolitan Minor3": [0, 1, 2, 3, 5, 7, 8, 11],
    "Hungarian Minor b2": [0, 1, 2, 3, 6, 7, 8, 11],
    "JG Octatonic": [0, 1, 3, 4, 5, 7, 9, 10],
    "JG Octatonic all 3b": [0, 1, 3, 4, 5, 7, 9, 10],
    "Lydian b3": [0, 2, 3, 4, 6, 7, 9, 11],
    "Lydian Dim b7": [0, 2, 3, 4, 6, 7, 9, 10],
    "Lydian Dominant alternate": [0, 2, 4, 6, 7, 9, 10, 11],
    "Magen Abot": [0, 1, 3, 4, 6, 8, 9, 11],
    "Magen Abot (3b 2#)": [0, 1, 3, 4, 6, 8, 9, 11],
    "Magen Abot all flats": [0, 1, 3, 4, 6, 8, 9, 11],
    "Magen Abot all sharps": [0, 1, 3, 4, 6, 8, 9, 11],
    "Maqam Hijaz": [0, 1, 4, 5, 7, 8, 10, 11],
    "Maqam Shadd'araban 1": [0, 1, 3, 4, 5, 6, 9, 10],
    "Maqam Shadd'araban 2": [0, 1, 3, 4, 5, 6, 9, 10],
    "Minor Bebop 1": [0, 2, 3, 4, 5, 7, 9, 10],
    "Minor Bebop 2": [0, 2, 3, 4, 5, 7, 9, 10],
    "Minor Gypsy": [0, 2, 3, 6, 7, 8, 10, 11],
    "Neveseri 1": [0, 1, 3, 6, 7, 8, 10, 11],
    "Neveseri 2": [0, 1, 3, 6, 7, 8, 10, 11],
    "Oriental 2": [0, 1, 4, 5, 6, 9, 10, 11],
    "Phrygian Aeolian 1": [0, 1, 2, 3, 5, 7, 8, 10],
    "Phrygian Aeolian 2": [0, 1, 2, 3, 5, 7, 8, 10],
    "Phrygian Locrian 1": [0, 1, 3, 5, 6, 7, 8, 10],
    "Phrygian Locrian 2": [0, 1, 3, 5, 6, 7, 8, 10],
    "Phrygian Major 1": [0, 1, 3, 4, 5, 7, 8, 10],
    "Phrygian Major 2": [0, 1, 3, 4, 5, 7, 8, 10],
    "Prokofiev 1": [0, 1, 3, 5, 6, 8, 10, 11],
    "Prokofiev 2": [0, 1, 3, 5, 6, 8, 10, 11],
    "Shostakovich 1": [0, 1, 3, 4, 6, 7, 9, 11],
    "Shostakovich 2": [0, 1, 3, 4, 6, 7, 9, 11],
    "Shostakovich 3": [0, 1, 3, 4, 6, 7, 9, 11],
    "Spanish 8 Tones 1": [0, 1, 3, 4, 5, 6, 8, 10],
    "Spanish 8 Tones 2": [0, 1, 3, 4, 5, 6, 8, 10],
    "Spanish 8 Tones 3": [0, 1, 3, 4, 5, 6, 8, 10],
    "Utility Minor 1": [0, 2, 3, 5, 7, 8, 10, 11],
    "Utility Minor 2": [0, 2, 3, 5, 7, 8, 10, 11],
    "Zirafkend": [0, 2, 3, 5, 7, 8, 9, 11],
    "Whole-Half Dim": [0, 2, 3, 5, 6, 8, 9, 11],
    "Half-Whole Dim": [0, 1, 3, 4, 6, 7, 9, 10],
    "Japanese": [0, 2, 4, 5, 6, 7, 9, 11],
    "Major Bebop": [0, 2, 4, 5, 7, 8, 9, 11],
    "Mixolydian Bebop 1": [0, 2, 4, 5, 7, 9, 10, 11],
    "Mixolydian Bebop 2": [0, 2, 4, 5, 6, 7, 9, 10],
    "Blues Enneatonic": [0, 2, 3, 4, 5, 6, 7, 9, 10],
    "Chromatic Bebop 1": [0, 1, 2, 4, 5, 7, 9, 10, 11],
    "Chromatic Bebop 2": [0, 1, 2, 4, 5, 7, 9, 10, 11],
    "Chromatic Diatonic Dorian 1": [0, 1, 2, 3, 5, 7, 8, 9, 10],
    "Chromatic Diatonic Dorian 2": [0, 1, 2, 3, 5, 7, 8, 9, 10],
    "Chromatic NonaMirror": [0, 1, 2, 3, 4, 5, 6, 7, 8],
    "Chromatic Permuted Diatonic": [0, 1, 2, 4, 5, 7, 8, 9, 11],
    "Full Minor": [0, 2, 3, 5, 7, 8, 9, 10, 11],
    "Full Minor all flats": [0, 2, 3, 5, 7, 8, 9, 10, 11],
    "Genus Chromaticum 1": [0, 1, 3, 4, 5, 7, 8, 9, 11],
    "Genus Chromaticum 2": [0, 1, 3, 4, 5, 7, 8, 9, 11],
    "Genus Chromaticum 3": [0, 1, 3, 4, 5, 7, 8, 9, 11],
    "Houseini 1": [0, 2, 3, 4, 5, 7, 9],
    "Houseini 2": [0, 2, 3, 4, 5, 7, 8, 9, 10],
    "Kiourdi": [0, 2, 3, 5, 6, 7, 8, 9, 10],
    "Lydian Mixolydian 1": [0, 2, 4, 5, 6, 7, 9, 10, 11],
    "Lydian Mixolydian 2": [0, 2, 4, 5, 6, 7, 9, 10, 11],
    "Moorish Phrygian 1": [0, 1, 4, 5, 7, 8, 10, 11],
    "Moorish Phrygian 2": [0, 1, 3, 4, 5, 7, 8, 10, 11],
    "Moorish Phrygian 3": [0, 1, 4, 5, 7, 8, 10, 11],
    "Moorish Phrygian 4": [0, 1, 3, 4, 5, 7, 8, 10, 11],
    "Moorish Phrygian 5": [0, 1, 3, 4, 5, 7, 8, 10, 11],
    "Symmetrical Nonatonic 1": [0, 1, 2, 4, 6, 7, 8, 10, 11],
    "Symmetrical Nonatonic 2": [0, 1, 2, 4, 6, 7, 8, 10, 11],
    "untitled Nonatonic 1": [0, 1, 2, 3, 5, 6, 7, 8, 9],
    "untitled Nonatonic 2": [0, 1, 3, 4, 5, 6, 7, 9, 10],
    "untitled Nonatonic 3": [0, 1, 3, 4, 5, 6, 7, 9, 10],
    "untitled Nonatonic 4": [0, 1, 3, 4, 5, 6, 7, 9, 10],
    "Youlan 1": [0, 1, 2, 4, 5, 6, 7, 9, 10],
    "Youlan 2": [0, 1, 2, 4, 5, 6, 7, 9, 10],
    "Untitled Decatonic 1": [0, 2, 3, 4, 5, 7, 8, 9, 10, 11],
    "Untitled Decatonic 2": [0, 2, 3, 4, 5, 6, 7, 9, 10, 11],
    "Untitled Decatonic 3": [0, 1, 3, 4, 5, 6, 7, 8, 10, 11],
    "Untitled Decatonic 3": [0, 1, 3, 4, 5, 6, 8, 9, 10, 11],
    "Untitled Decatonic 4": [0, 1, 2, 3, 5, 6, 7, 8, 10, 11],
    "Untitled Decatonic 5": [0, 1, 2, 3, 5, 6, 7, 8, 9, 10],
    "Untitled Decatonic 6": [0, 1, 2, 4, 5, 6, 7, 9, 10, 11],
    "Untitled Decatonic 7": [0, 1, 2, 4, 5, 6, 7, 8, 9, 11],
    "Untitled Decatonic 8": [0, 1, 2, 3, 4, 6, 7, 8, 9, 11],
    "Untitled Decatonic 9": [0, 1, 2, 3, 4, 5, 7, 8, 9, 10],
    "Chromatic DecaMirror 1": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Chromatic DecaMirror 2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Major & Minor mixed": [0, 2, 3, 4, 5, 7, 8, 9, 10, 11],
    "Minor Pentatonic Decatonic": [0, 2, 3, 4, 5, 6, 7, 9, 10, 11],
    "Pan Diminished Blues": [0, 1, 2, 3, 4, 6, 7, 9, 10, 11],
    "Pan Lydian": [0, 2, 3, 4, 5, 6, 7, 8, 9, 11],
    "Symmetrical Decatonic": [0, 1, 2, 4, 5, 6, 7, 8, 10, 11],
}


def get_scale_notes(scale, tonic="C"):  # type: ignore
    # i = notes.index(tonic)
    # tscale = notes[i:] + notes[:i]
    hscale = m21.scale.ChromaticScale(tonic)
    return [hscale.pitches[j].name for j in scales[scale]]


def get_enharmonic(note_name: str) -> str:
    en_dict = {
        "c-": "b",
        "c#": "d-",
        "d#": "e-",
        "e": "f-",
        "e#": "f",
        "f#": "g-",
        "g#": "a-",
        "a#": "b-",
        "b#": "c",
        "d": "c##",
        "g": "a--",
        "a": "b--",
    }
    en_dict.update(dict(zip(en_dict.values(), en_dict.keys())))
    return en_dict[note_name.lower()]


notesx = notes + tuple(get_enharmonic(n) for n in notes)
