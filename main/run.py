import sys
import pygame
from pygame.locals import *
from Game.object import Player, Window, Operation, Background, Fist
from Game.configuration import IMAGE

pygame.init()


def run():
    window = Window('first python game!')
    screen = window.screen
    background = Background(IMAGE.get('background')).background
    player = Player(IMAGE.get('player'))
    fist = Fist(IMAGE.get('fist'))
    player.x_speed = 10
    player.y_speed = 0
    allsprites = pygame.sprite.RenderPlain((player, fist))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()

    while 1:
        """
            responding the mouse click event in order to prevent the window gets stuck
        """
        clock.tick(30)
        operation = Operation()
        player.move()
        for event in operation.operations:
            if event.type == operation.quit:
                pygame.quit()
                sys.exit()
            if event.type == operation.keydown and event.key == operation.key_escape:
                going = False
            elif event.type == operation.mouse_button_down:
                print("get mouse button down event")
                if fist.punch(player):
                    print("hitted")  # punch
                else:
                    print('miss')  # miss
            elif event.type == operation.mouse_button_up:
                fist.unpunch()

        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    run()
