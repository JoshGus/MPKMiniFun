import pygame

pygame.mixer.init()

sound = pygame.mixer.Sound("Sounds/ARC-EpicLoot1.mp3")
sound.play()

input("Press enter to quit")