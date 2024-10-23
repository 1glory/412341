import sys

import pygame


class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound

    def __init__(self) -> None:
        if "win" in sys.platform:
            ext = "wav"
        else:
            ext = "ogg"

        self.die = pygame.mixer.Sound(f"assets/audio/aint.{ext}")
        self.hit = pygame.mixer.Sound(f"assets/audio/bruh.{ext}")
        self.point = pygame.mixer.Sound(f"assets/audio/ayo.{ext}")
        self.swoosh = pygame.mixer.Sound(f"assets/audio/swoosh.{ext}")
        self.wing = pygame.mixer.Sound(f"assets/audio/wing.{ext}")
