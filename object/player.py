import pygame
from typing import Union
from Game.object.base import Image, Sprite


class Player(Image, Sprite):

    def __init__(self, image):
        Image.__init__(self, image)
        Sprite.__init__(self)
        self.player = self.image
        self.rect = self.player.get_rect().move(1, 40)
        self.__x_speed = 0
        self.__y_speed = 0

    @property
    def x_speed(self):
        return self.__x_speed

    @x_speed.setter
    def x_speed(self, speed):
        self.__x_speed = speed

    @property
    def y_speed(self):
        return self.__y_speed

    @y_speed.setter
    def y_speed(self, speed: Union[int, float]):
        self.__y_speed = speed

    def move(self):
        self.rect = self.rect.move(self.__x_speed, self.__y_speed)
        if self.rect.right > 600:
            self.rect.left = 0
