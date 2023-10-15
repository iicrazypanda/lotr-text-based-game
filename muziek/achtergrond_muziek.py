import os
import pygame


def speel_achtergrond_muziek():
    cwd = os.getcwd()
    muziek_path = cwd + "/muziek/rivendell_muziek.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(muziek_path)
    pygame.mixer.music.play(-1)
