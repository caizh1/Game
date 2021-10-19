"""
    basic class
"""

import pygame


class Image:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert()
