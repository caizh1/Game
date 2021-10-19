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

    while 1:
        """
            responding the mouse click event in order to prevent the window gets stuck
        """
        operation = Operation()
        operation.quit()
        player.move()
        for event in operation.operations:
            if event.type == operation.event_table.get('keydown') and event.key == operation.event_table.get('escape'):
                going = False
            elif event.type == operation.event_table.get('mouse_button_down'):
                if fist.punch(player):
                    print("hitted")  # punch
                else:
                    print('miss')  # miss
            elif event.type == operation.event_table.get('mouse_button_up'):
                fist.unpunch()

        allsprites.update()
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    run()
