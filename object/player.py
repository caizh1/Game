import pygame
from typing import Union


class Player:

    def __init__(self, image):
        self.player = pygame.image.load(image).convert()
        self.postion = self.player.get_rect().move(1, 40)
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
        self.postion = self.postion.move(self.__x_speed, self.__y_speed)
        if self.postion.right > 600:
            self.postion.left = 0
