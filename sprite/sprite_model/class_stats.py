import pygame
from .base_sprite import BaseSprite


class StatsRect(BaseSprite):
    def __init__(self, rect_height, rect_length, bold_size, screen, background, image=None,
                 initial_position: tuple = (),
                 *group: pygame.sprite.Group):
        super(StatsRect, self).__init__(rect_height, rect_length, screen, background, image,
                                        initial_position=initial_position,
                                        *group)
        self.bold_size = bold_size

    def draw_rect(self, color: tuple):
        """
        :param color: rgb(x, x, x)
        :return:
        """
        outline_rect = pygame.Rect(self._initial_position[0], self._initial_position[1], self.width, self.height)
        pygame.draw.rect(self.screen, color, outline_rect, self.bold_size)

    def fill_rect(self, value, color):
        """
        :param value: how long you want to fill the rect
        :param color: rgb(x, x, x)
        :return:
        """
        fill_rect = pygame.Rect(
            self._initial_position[0] + self.bold_size,
            self._initial_position[1] + self.bold_size,
            value - self.bold_size,
            self.height - self.bold_size * 2
        )
        pygame.draw.rect(self.screen, color, fill_rect)
