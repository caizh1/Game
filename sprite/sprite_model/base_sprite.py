import sys
import pygame


class BaseSprite(pygame.sprite.Sprite):
    def __init__(
            self, height, width, screen, background, image: str = None, initial_position: tuple = (),
            *group: pygame.sprite.Group
    ):
        """
        :param height:
        :param width:
        :param screen:
        :param background:
        :param image: filename
        :param initial_position:
        :param group:
        """
        super(BaseSprite, self).__init__(*group)
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
        if self._image:
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
    def __init__(
            self, speed, height, width, image, screen, background,
            initial_position: tuple, *group):
        super(BaseCharacter, self).__init__(height, width, screen, background, image, initial_position, *group)
        self.speed = speed

    def stop_across_obstacle_left(self, sprite_group):
        for sprite in sprite_group:
            if pygame.sprite.collide_rect(self, sprite):
                if self._sprite_rect.left <= sprite.rect.right:
                    self._sprite_rect.left = sprite.rect.right

    def stop_across_obstacle_right(self, sprite_group):
        # check if collide the sprite_group
        for sprite in sprite_group:
            if pygame.sprite.collide_rect(self, sprite):
                if self._sprite_rect.right >= sprite.rect.left:
                    self._sprite_rect.right = sprite.rect.left

    def stop_across_obstacle_up(self, sprite_group):
        # check if collide the sprite_group
        for sprite in sprite_group:
            if pygame.sprite.collide_rect(self, sprite):
                if self._sprite_rect.top <= sprite.rect.bottom:
                    self._sprite_rect.top = sprite.rect.bottom

    def stop_across_obstacle_down(self, sprite_group):
        # check if collide the sprite_group
        for sprite in sprite_group:
            if pygame.sprite.collide_rect(self, sprite):
                if self._sprite_rect.bottom >= sprite.rect.top:
                    self._sprite_rect.bottom = sprite.rect.top

    def check_collide_with_group(self, sprite_group: pygame.sprite.Group):
        for sprite in sprite_group:
            if pygame.sprite.collide_rect(self, sprite):
                return sprite
            else:
                return

    def stop_moving_out_screen(self):
        screen_rect = self.screen.get_rect()
        if self._sprite_rect.left < 0:
            self._sprite_rect.left = 0
        if self._sprite_rect.right > screen_rect.right:
            self._sprite_rect.right = screen_rect.right
        if self._sprite_rect.top < 0:
            self._sprite_rect.top = 0
        if self._sprite_rect.bottom > screen_rect.bottom:
            self._sprite_rect.bottom = screen_rect.bottom


class BaseObstacle(BaseSprite):
    def __init__(
            self, height, width, screen, background, image,
            initial_position: tuple, *group):
        super(BaseObstacle, self).__init__(height, width, screen, background, image, initial_position, *group)


class BaseItem(BaseSprite):
    def __init__(
            self, height, width, screen, background, image,
            initial_position: tuple, *group):
        super(BaseItem, self).__init__(height, width, screen, background, image, initial_position, *group)


class BaseStatsRect(BaseSprite):
    def __init__(
            self, height, width, screen, background,
            initial_position: tuple, *group):
        super(BaseStatsRect, self).__init__(
            height,
            width,
            screen,
            background,
            initial_position=initial_position,
            *group
        )
