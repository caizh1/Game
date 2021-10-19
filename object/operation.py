import sys
import pygame


class Operation:
    def __init__(self):
        self.event_table = {
            'quit': pygame.QUIT,
            'keydown': pygame.KEYDOWN,
            'key_escape': pygame.K_ESCAPE,
            'mouse_button_down': pygame.MOUSEBUTTONDOWN,
            'mouse_button_up': pygame.MOUSEBUTTONUP,
        }

    @property
    def operations(self):
        return pygame.event.get()

    def quit(self):
        for operation in self.operations:
            if operation.type == self.event_table['quit']:
                pygame.quit()
                sys.exit()
