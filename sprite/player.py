import pygame.sprite

from .base_sprite import BaseCharacter


class Kitty(BaseCharacter):

    def erase(self):
        self.screen.blit(self.background, self._sprite_rect, self._sprite_rect)

    def move_left(self, sprite_group: pygame.sprite.Group):
        """
        :param sprite_group:
        :return:
        this function is to move the object of this class. Stop this object if it collides the sprite_group.
        """
        screen_rect = self.screen.get_rect()
        self.erase()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(-self.speed, 0)
            if self._sprite_rect.left < 0:
                self._sprite_rect.left = 0

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.left <= sprite.rect.right:
                        self._sprite_rect.left = sprite.rect.right

    def move_right(self, sprite_group: pygame.sprite.Group):
        screen_rect = self.screen.get_rect()
        self.erase()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(self.speed, 0)
            if self._sprite_rect.right > screen_rect.right:
                self._sprite_rect.right = screen_rect.right

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.right >= sprite.rect.left:
                        self._sprite_rect.right = sprite.rect.left

    def move_up(self, sprite_group: pygame.sprite.Group):
        screen_rect = self.screen.get_rect()
        self.erase()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(0, -self.speed)
            if self._sprite_rect.top < 0:
                self._sprite_rect.top = 0

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.top <= sprite.rect.bottom:
                        self._sprite_rect.top = sprite.rect.bottom

    def move_down(self, sprite_group: pygame.sprite.Group):
        screen_rect = self.screen.get_rect()
        self.erase()
        if self._sprite_surface:
            self._sprite_rect = self._sprite_rect.move(0, self.speed)
            if self._sprite_rect.bottom > screen_rect.bottom:
                self._sprite_rect.bottom = screen_rect.bottom

            # check if collide the sprite_group
            for sprite in sprite_group:
                if pygame.sprite.collide_rect(self, sprite):
                    if self._sprite_rect.bottom >= sprite.rect.top:
                        self._sprite_rect.bottom = sprite.rect.top
