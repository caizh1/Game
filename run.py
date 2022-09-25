import sys
import pygame
from config import cfg
from sprite.sprite_model.player import Kitty
from sprite.sprite_utils.obstacle import obstacles_generator


# create screen and background
screen = pygame.display.set_mode(cfg.SCREEN_DEFAULT, pygame.RESIZABLE)
background_ = pygame.image.load("./images/background.png")
background = pygame.transform.scale(background_, cfg.SCREEN_DEFAULT).convert_alpha()
screen.blit(background, (0, 0))


# create player
kitty = Kitty(5, 120, 60, "./images/player_cat_1.png", screen, background, (500, 400))
kitty_group = pygame.sprite.Group()
kitty_group.add(kitty)
kitty_group.draw(screen)


# create obstacles
obstacle_group = pygame.sprite.Group()
generator_object = obstacles_generator(
    (50, 50),
    "./images/obstacle_1.png",
    5,
    "right",
    (100, 0),
    screen,
    background,
    obstacle_group
)
generator_object = obstacles_generator(
    (50, 50), "./images/obstacle_1.png",
    5,
    "down",
    generator_object.last_object_position,
    screen,
    background,
    obstacle_group)

obstacle_group.draw(screen)


# update screen and set frame per sec
pygame.display.update()
fps = 60
clock = pygame.time.Clock()


def main():
    while 1:

        # using get_pressed instead of listen pygame key down event in order to implement the smooth movement
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT]:
            kitty.move_left(obstacle_group)
        if pressed_key[pygame.K_RIGHT]:
            kitty.move_right(obstacle_group)
        if pressed_key[pygame.K_UP]:
            kitty.move_up(obstacle_group)
        if pressed_key[pygame.K_DOWN]:
            kitty.move_down(obstacle_group)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        screen.blit(kitty.image, kitty.rect)
        clock.tick(fps)
        pygame.display.update()


main()
