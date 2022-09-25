import pygame
from sprite.sprite_model.base_sprite import BaseItem


class KittyCan(BaseItem):

    def erase(self):
        self.screen(self.background, self._sprite_rect, self._sprite_rect)
