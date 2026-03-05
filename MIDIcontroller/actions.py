import pygame
from pathlib import Path

# Initialize mixer once
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

# Locate sounds folder relative to project root
SOUNDS_DIR = Path(__file__).resolve().parent.parent / "Sounds"

# Load sounds
pad_sounds = {
    "PAD_1": pygame.mixer.Sound(SOUNDS_DIR / "ARC-EpicLoot1.mp3"),
    "PAD_2": pygame.mixer.Sound(SOUNDS_DIR / "ARC-EpicLoot2.mp3"),
    "PAD_3": pygame.mixer.Sound(SOUNDS_DIR / "ARC-EpicLoot3.mp3"),
    "PAD_4": pygame.mixer.Sound(SOUNDS_DIR / "ARC-LegLoot.mp3"),
    "PAD_5": pygame.mixer.Sound(SOUNDS_DIR / "ARC-cam.mp3"),
}

# Optional: adjust volume (0.0–1.0)
for sound in pad_sounds.values():
    sound.set_volume(0.9)


def handle_action(event):
    """
    Handle parsed MIDI events.
    """

    event_type = event.get("type")

    if event_type == "pad":

        pad = event.get("pad")

        if pad in pad_sounds:
            print(f"Playing sound for {pad}")
            pad_sounds[pad].play()

        else:
            print(f"No sound mapped for {pad}")

    elif event_type == "note_on":

        print(f"Key pressed: {event['note']} velocity={event['velocity']}")

    elif event_type == "knob":

        print(f"Knob {event['control']} value={event['value']}")