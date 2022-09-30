import sys
import pygame
from config import cfg
from sprite.sprite_model.player import Kitty
from sprite.sprite_model.item import KittyCan
from sprite.sprite_utils.obstacle import obstacles_generator

from sprite.sprite_model.stats_rect import StatsRect
# create screen and background
screen = pygame.display.set_mode(cfg.SCREEN_DEFAULT, pygame.RESIZABLE)
background_ = pygame.image.load("./images/background.png")
background = pygame.transform.scale(background_, cfg.SCREEN_DEFAULT).convert_alpha()
screen.blit(background, (0, 0))

# create
item_group = pygame.sprite.Group()
kitty_can = KittyCan(50, 50, screen, background, "./images/item_1.png", (300, 200), item_group)
item_group.draw(screen)

# create player
kitty_images = list()
for index in range(0, 8):
    image = f"./images/kitty_{index}.png"
    kitty_images.append(image)
kitty_group = pygame.sprite.Group()
kitty = Kitty(3, 90, 90, kitty_images, screen, background, (500, 400), kitty_group)
kitty_group.draw(screen)


# create obstacles
obstacle_group = pygame.sprite.Group()
generator_object = obstacles_generator(
    (30, 30),
    "./images/obstacle_1.png",
    5,
    "right",
    (150, 0),
    screen,
    background,
    obstacle_group
)
generator_object = obstacles_generator(
    (30, 30), "./images/obstacle_1.png",
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

# create stat rect
stat_rect_health = StatsRect(20, 102, 2, screen, background, initial_position=(10, 10))
stat_rect_health.draw_rect((255, 255, 255), "./images/health_1.png", 20)


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

        stat_rect_health.fill_rect(kitty.health, (255, 0, 0))

        # stat_rect_mood = StatsRect(20, 102, 2, screen, background, initial_position=(10, 30))
        # stat_rect_mood.draw_rect((255, 255, 255))
        # stat_rect_mood.fill_rect(kitty.mood, (0, 255, 0))
        #
        # stat_rect_energy = StatsRect(20, 102, 2, screen, background, initial_position=(10, 50))
        # stat_rect_energy.draw_rect((255, 255, 255))
        # stat_rect_energy.fill_rect(kitty.energy, (0, 0, 0))
        #
        # stat_rect_hungry = StatsRect(20, 102, 2, screen, background, initial_position=(10, 70))
        # stat_rect_hungry.draw_rect((255, 255, 255))
        # stat_rect_hungry.fill_rect(kitty.hungry, (255, 128, 0))
        #
        # stat_rect_thirsty = StatsRect(20, 102, 2, screen, background, initial_position=(10, 90))
        # stat_rect_thirsty.draw_rect((255, 255, 255))
        # stat_rect_thirsty.fill_rect(kitty.thirsty, (0, 0, 255))

        screen.blit(kitty.image, kitty.rect)

        kitty.eat(item_group)

        clock.tick(fps)
        pygame.display.update()


main()
