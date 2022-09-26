import pygame
from sprite.sprite_model.base_sprite import BaseItem


class KittyCan(BaseItem):

    def erase(self):
        for group in self.groups():
            group.remove(self)
        self.screen.blit(self.background, self._sprite_rect, self._sprite_rect)
