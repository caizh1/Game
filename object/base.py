"""
    basic class
"""

import pygame


class Image:
    def __init__(self, image):
        self.__image = pygame.image.load(image).convert()

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, color_key):
        if color_key is not None:
            if color_key == -1:
                color_key = self.__image.get_at((0, 0))
        self.__image.set_colorkey(color_key, pygame.RLEACCEL)


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        pass
