import sys
import pygame


class Operation:
    def __init__(self):
        self.event_table = {
            'quit': pygame.QUIT
        }

    @property
    def operations(self):
        return pygame.event.get()

    def quit(self):
        for operation in self.operations:
            if operation.type == self.event_table['quit']:
                pygame.quit()
                sys.exit()
