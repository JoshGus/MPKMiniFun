import pygame.midi


class MidiListener:
    def __init__(self):
        pygame.midi.init()

        self.device_id = self._find_device()
        self.midi = pygame.midi.Input(self.device_id)

        print(f"Connected to device {self.device_id}")

    def _find_device(self):
        for i in range(pygame.midi.get_count()):
            info = pygame.midi.get_device_info(i)
            name = info[1].decode()

            if "MPK" in name and info[2] == 1:
                return i

        raise RuntimeError("MPK Mini not found")

    def listen(self):
        while True:
            if self.midi.poll():
                events = self.midi.read(10)

                for event in events:
                    yield event