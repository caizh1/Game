import pygame
from .base_sprite import BaseCharacter
from sprite.sprite_model.item import KittyCan


class Kitty(BaseCharacter):
    def __init__(
            self, speed, height, width, image: list, screen, background,
            initial_position: tuple, group: pygame.sprite.Group = None
    ):
        self.health = 50
        self.mood = 100
        self.hungry = 100
        self.energy = 100
        self.thirsty = 100
        self.__last_update = pygame.time.get_ticks()
        super(Kitty, self).__init__(speed, height, width, image, screen, background, initial_position, group)
        self._image = image
        self.__direction = "right"
        self.__last_position = initial_position
        self.__current_image_index = 0

    def __update(self):
        delay = 100
        now = pygame.time.get_ticks()
        if now > self.__last_update + delay:
            self.__last_update = now
            self.__current_image_index += 1
            if self.__current_image_index > len(self._image) - 1:
                self.__current_image_index = 0
            sprite_surface = pygame.image.load(self._image[self.__current_image_index])
            self._sprite_surface = pygame.transform.scale(sprite_surface, (self.height, self.width)).convert_alpha()
            self._sprite_rect = self._sprite_surface.get_rect()
            if self.__direction == "left":
                self._sprite_surface = pygame.transform.flip(self._sprite_surface, True, False)
            self._sprite_rect.topleft = self.__last_position

    def _create(self):
        sprite_surface = pygame.image.load(self._image[0])
        self._sprite_surface = pygame.transform.scale(sprite_surface, (self.height, self.width)).convert_alpha()
        self._sprite_rect = self._sprite_surface.get_rect()
        self._sprite_rect.topleft = self._initial_position
        self.__last_position = self.topleft

    def erase(self):
        self.screen.blit(self.background, self._sprite_rect, self._sprite_rect)

    def move_left(self, sprite_group: pygame.sprite.Group):
        """
        :param sprite_group:
        :return:
        this function is to move the object of this class. Stop this object if it collides the sprite_group.
        """

        # change the image direction when doing movement
        if self.__direction != "left":
            self._sprite_surface = pygame.transform.flip(self._sprite_surface, True, False)
            self.__direction = "left"

        screen_rect = self.screen.get_rect()
        self.erase()
        self.__update()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(-self.speed, 0)
            if self._sprite_rect.left < 0:
                self._sprite_rect.left = 0

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.left <= sprite.rect.right:
                        self._sprite_rect.left = sprite.rect.right
        self.__last_position = self.topleft

    def move_right(self, sprite_group: pygame.sprite.Group):
        if self.__direction != "right":
            self._sprite_surface = pygame.transform.flip(self._sprite_surface, True, False)
            self.__direction = "right"

        screen_rect = self.screen.get_rect()
        self.erase()
        self.__update()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(self.speed, 0)
            if self._sprite_rect.right > screen_rect.right:
                self._sprite_rect.right = screen_rect.right

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.right >= sprite.rect.left:
                        self._sprite_rect.right = sprite.rect.left

        self.__last_position = self.topleft

    def move_up(self, sprite_group: pygame.sprite.Group):
        screen_rect = self.screen.get_rect()
        self.erase()
        self.__update()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(0, -self.speed)
            if self._sprite_rect.top < 0:
                self._sprite_rect.top = 0

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.top <= sprite.rect.bottom:
                        self._sprite_rect.top = sprite.rect.bottom

        self.__last_position = self.topleft

    def move_down(self, sprite_group: pygame.sprite.Group):
        screen_rect = self.screen.get_rect()
        self.erase()
        self.__update()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(0, self.speed)
            if self._sprite_rect.bottom > screen_rect.bottom:
                self._sprite_rect.bottom = screen_rect.bottom

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.bottom >= sprite.rect.top:
                        self._sprite_rect.bottom = sprite.rect.top

        self.__last_position = self.topleft

    def eat(self, sprite_group):
        item = self.check_collide_with_group(sprite_group)
        if item:
            if isinstance(item, KittyCan):
                self.health += 30
                item.erase()
