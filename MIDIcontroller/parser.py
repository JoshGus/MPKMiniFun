NOTE_NAMES = [
    'C', 'C#', 'D', 'D#', 'E', 'F',
    'F#', 'G', 'G#', 'A', 'A#', 'B'
]

PAD_MAP = {
    36: "PAD_1",
    37: "PAD_2",
    38: "PAD_3",
    39: "PAD_4",
    40: "PAD_5",
    41: "PAD_6",
    42: "PAD_7",
    43: "PAD_8"
}


def note_to_name(note):
    octave = (note // 12) - 1
    name = NOTE_NAMES[note % 12]
    return f"{name}{octave}"


def parse_event(event):

    data = event[0]
    status = data[0]
    note = data[1]
    value = data[2]

    if status == 144 and value > 0:

        if note in PAD_MAP:
            return {
                "type": "pad",
                "pad": PAD_MAP[note]
            }

        return {
            "type": "note_on",
            "note": note_to_name(note),
            "velocity": value
        }

    elif status == 176:
        return {
            "type": "knob",
            "control": note,
            "value": value
        }

    return None