import sys
import pygame


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, height, width, image, screen, background, initial_position: tuple):
        super(BaseSprite, self).__init__()
        self.height = height
        self.width = width
        self._image = image
        self.screen = screen
        self.background = background
        self._sprite_surface = pygame.surface.Surface
        self._sprite_rect = pygame.rect.Rect
        self._initial_position = initial_position
        self._create()

    def _create(self):
        sprite_surface = pygame.image.load(self._image)
        self._sprite_surface = pygame.transform.scale(sprite_surface, (self.height, self.width)).convert_alpha()
        self._sprite_rect = self._sprite_surface.get_rect()
        self._sprite_rect.topleft = self._initial_position

    @property
    def rect(self):
        return self._sprite_rect

    @property
    def image(self):
        return self._sprite_surface


class BaseCharacter(BaseSprite):
    def __init__(self, speed, height, width, image, screen, background, initial_position: tuple):
        super(BaseCharacter, self).__init__(height, width, image, screen, background, initial_position)
        self.speed = speed

    def move_left(self, sprite):
        pass

    def move_right(self, sprite):
        pass

    def move_up(self, sprite):
        pass

    def move_down(self, sprite):
        pass


class BaseObstacle(BaseSprite):
    def __init__(self, height, width, image, screen, background, initial_position: tuple):
        super(BaseObstacle, self).__init__(height, width, image, screen, background, initial_position)
