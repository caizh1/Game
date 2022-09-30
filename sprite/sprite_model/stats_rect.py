import pygame
from .base_sprite import BaseStatsRect


class StatsRect(BaseStatsRect):
    def __init__(self, rect_height, rect_length, bold_size, screen, background,
                 initial_position: tuple = (),
                 *group: pygame.sprite.Group):
        super(StatsRect, self).__init__(rect_height, rect_length, screen, background,
                                        initial_position=initial_position,
                                        *group)
        self.bold_size = bold_size

    def _create(self):
        self._sprite_rect = pygame.Rect(self._initial_position[0], self._initial_position[1], self.width, self.height)

    def draw_rect(self, color: tuple, image=None, image_width=None):
        """
        :param image: file name
        :param image_width:
        :param color: rgb(x, x, x)
        :return:
        """
        image_rect = None
        if image:
            sprite_surface = pygame.image.load(image)
            image_surface = pygame.transform.scale(sprite_surface, (image_width, self.height)).convert_alpha()
            image_rect = image_surface.get_rect()
            image_rect.topleft = self._initial_position
            self.screen.blit(image_surface, image_rect)

        offset = 5
        if image_rect:
            self._sprite_rect = pygame.Rect(
                image_rect.right + offset,
                self._initial_position[1],
                self.width,
                self.height
            )

        pygame.draw.rect(self.screen, color, self._sprite_rect, self.bold_size)

    def fill_rect(self, value, color):
        """
        :param value: how long you want to fill the rect
        :param color: rgb(x, x, x)
        :return:
        """
        fill_rect = pygame.Rect(
            self._sprite_rect.left + self.bold_size,
            self._initial_position[1] + self.bold_size,
            value - self.bold_size,
            self.height - self.bold_size * 2
        )
        pygame.draw.rect(self.screen, color, fill_rect)
