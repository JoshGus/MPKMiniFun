NOTE_NAMES = [
    'C', 'C#', 'D', 'D#', 'E', 'F',
    'F#', 'G', 'G#', 'A', 'A#', 'B'
]

PAD_MAP = {
    48: "PAD_1",
    50: "PAD_2",
    52: "PAD_3",
    53: "PAD_4",
    55: "PAD_5",
    57: "PAD_6",
    59: "PAD_7",
    60: "PAD_8"
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

    # NOTE ON
    if 144 <= status < 160 and value > 0:

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

    # CONTROL CHANGE (knobs)
    elif 176 <= status < 192:
        return {
            "type": "knob",
            "control": note,
            "value": value
        }

    return None