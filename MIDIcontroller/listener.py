import pygame
import pygame.midi
import time


class MidiListener:

    def __init__(self):

        pygame.init()
        pygame.midi.init()

        self.device_id = self._find_device()

        print(f"\nOpening MIDI input device {self.device_id}")

        self.midi = pygame.midi.Input(self.device_id)

        print("Listening for MIDI input...\n")

    def _find_device(self):

        print("Available MIDI devices:\n")

        for i in range(pygame.midi.get_count()):

            info = pygame.midi.get_device_info(i)
            name = info[1].decode()
            is_input = info[2]

            print(i, info)

            if "MPK" in name and is_input:
                return i

        raise RuntimeError("MPK Mini not found")

    def listen(self):

        print("Listening for MIDI events...")

        while True:

            events = self.midi.read(10)

            if events:
                for event in events:
                    yield event

            time.sleep(0.001)