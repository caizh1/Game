import pygame
from pygame.locals import *
from Game.object.player import Player
from Game.object.window import Window, Background
from Game.configuration import settings

pygame.init()


def run():
    screen = Window().screen
    background = Background(settings.IMAGE.get('background')).background
    player = Player(settings.IMAGE.get('player'))
    player.x_speed = 10
    player.y_speed = 0
    screen.blit(background, (0, 0))

    while 1:
        screen.blit(background, player.postion, player.postion)
        player.move()
        screen.blit(player.player, player.postion)
        pygame.display.update()
        pygame.time.delay(100)


if __name__ == '__main__':
    run()
