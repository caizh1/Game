import pygame
from pygame.locals import *
from Game.object import Player, Window, Operation, Background
from Game.configuration import IMAGE

pygame.init()


def run():
    screen = Window().screen
    background = Background(IMAGE.get('background')).background
    player = Player(IMAGE.get('player'))
    player.x_speed = 10
    player.y_speed = 0
    screen.blit(background, (0, 0))

    while 1:
        """
            responding the mouse click event in order to prevent the window gets stuck
        """
        operation = Operation()
        operation.quit()
        screen.blit(background, player.postion, player.postion)
        player.move()
        screen.blit(player.player, player.postion)
        pygame.display.update()
        pygame.time.delay(100)


if __name__ == '__main__':
    run()
