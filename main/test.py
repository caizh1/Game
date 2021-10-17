import pygame
from pygame.locals import *

pygame.init()


def create_screen(x_width, y_width):
    return pygame.display.set_mode((x_width, y_width))


def create_player(path):
    return pygame.image.load(path).convert()


def set_background(path):
    return pygame.image.load(path).convert()


class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos.left = 0
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0


screen = create_screen(640, 480)
player = create_player('../static/supermario.jpg')
background = set_background('../static/fire_background.jpg')
screen.blit(background, (0, 0))
player_pos = player.get_rect().move(1, 40)

while 1:
    screen.blit(background, player_pos, player_pos)
    player_pos = player_pos.move(1, 1)
    screen.blit(player, player_pos)
    pygame.display.update()
    pygame.time.delay(100)
