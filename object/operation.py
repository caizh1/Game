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

    @property
    def mouse_button_down(self):
        return self.event_table.get('mouse_button_down')

    @property
    def mouse_button_up(self):
        return self.event_table.get('mouse_button_up')

    @property
    def keydown(self):
        return self.event_table.get('key_down')

    @property
    def key_escape(self):
        return self.event_table.get('key_escape')

    @property
    def quit(self):
        return self.event_table.get('quit')
