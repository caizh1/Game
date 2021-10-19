import pygame
from Game.object.base import Image, Sprite


class Fist(Sprite, Image):
    def __init__(self, image):
        Image.__init__(self, image)
        Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.punching = 0

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.punching:
            """
                rect.move_ip() moves the original object, rect.move() creates a new object and moves it to destination
            """
            self.rect.move_ip(5, 10)

    def punch(self, target):
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        self.punching = 0
