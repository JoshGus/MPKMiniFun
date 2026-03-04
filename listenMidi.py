import pygame.midi

pygame.midi.init()

for i in range(pygame.midi.get_count()):
    info = pygame.midi.get_device_info(i)
    name = info[1].decode()

    if "MPK" in name and info[2] == 1:
        device_id = i
        break

midi = pygame.midi.Input(device_id)

print("Listening to MPK Mini...")

while True:
    if midi.poll():
        events = midi.read(10)
        for event in events:
            print(event)