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

    def __get_left(self):
        return self._sprite_rect.left

    def __set_left(self, left_position):
        self._sprite_rect.left = left_position

    def __get_right(self):
        return self._sprite_rect.right

    def __set_right(self, right_position):
        self._sprite_rect.right = right_position

    def __get_top(self):
        return self._sprite_rect.top

    def __set_top(self, top_position):
        self._sprite_rect.top = top_position

    def __get_bottom(self):
        return self._sprite_rect.bottom

    def __set_bottom(self, bottom_position):
        self._sprite_rect.bottom = bottom_position

    def __get_topleft(self):
        return self._sprite_rect.topleft

    def __set_topleft(self, topleft_position):
        self._sprite_rect.topleft = topleft_position

    left = property(__get_left, __set_left)
    right = property(__get_right, __set_right)
    top = property(__get_top, __set_top)
    bottom = property(__get_bottom, __set_bottom)
    topleft = property(__get_topleft, __set_topleft)


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


class BaseItem(BaseSprite):
    def __init__(self, height, width, image, screen, background, initial_position: tuple):
        super(BaseItem, self).__init__(height, width, image, screen, background, initial_position)
