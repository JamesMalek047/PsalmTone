from music21 import converter

def parse_music(file_path):
    score = converter.parse(file_path)
    notes = []

    for element in score.flat.notes:
        if element.isNote:
            pitch = element.pitch.midi
            duration = element.quarterLength
            notes.append((pitch, duration))
        elif element.isChord:
            for n in element.notes:
                pitch = n.pitch.midi
                duration = element.quarterLength
                notes.append((pitch, duration))

    return notes
def get_time_signature(file_path):
    score = converter.parse(file_path)
    first_part = score.parts[0]
    time_signature = first_part.recurse().getElementsByClass('TimeSignature')[0]
    
    return time_signature.numerator, time_signature.denominator
