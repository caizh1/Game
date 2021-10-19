import pygame
from Game.object.base import Image


class Window:

    def __init__(self, title):
        self.__width = 640
        self.__height = 480

        pygame.display.set_caption(title)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def screen(self):
        return pygame.display.set_mode((self.width, self.height))


class Background(Image):
    def __init__(self, image):
        super().__init__(image)
        self.__image = self.image

    @property
    def background(self):
        return self.__image
