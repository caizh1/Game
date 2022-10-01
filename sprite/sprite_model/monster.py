from random import randint
from .base_sprite import BaseCharacter


class BasicMonster(BaseCharacter):
    def __init__(self, speed, width, height, image, screen, background,
                 initial_position: tuple, *group):
        super(BasicMonster, self).__init__(speed, width, height, image, screen, background,
                                           initial_position, *group)
        self.health = 100
        self.__last_moving_direction = 2

    def move_up(self, sprite_group):
        status = False
        self._sprite_rect = self._sprite_rect.move(0, -self.speed)
        if self.stop_moving_out_screen() or self.stop_across_obstacle_up(sprite_group):
            status = True
        return status

    def move_down(self, sprite_group):
        status = False
        self._sprite_rect = self._sprite_rect.move(0, self.speed)
        if self.stop_moving_out_screen() or self.stop_across_obstacle_down(sprite_group):
            status = True
        return status

    def move_left(self, sprite_group):
        status = False
        self._sprite_rect = self._sprite_rect.move(-self.speed, 0)
        if self.stop_moving_out_screen() or self.stop_across_obstacle_left(sprite_group):
            status = True
        return status

    def move_right(self, sprite_group):
        status = False
        self._sprite_rect = self._sprite_rect.move(self.speed, 0)
        if self.stop_moving_out_screen() or self.stop_across_obstacle_right(sprite_group):
            status = True
        return status

    def check_touch_edge(self):
        screen_rect = self.screen.get_rect()
        if self._sprite_rect.left < 0:
            status = True
        elif self._sprite_rect.right > screen_rect.right:
            status = True
        elif self._sprite_rect.top < 0:
            status = True
        elif self._sprite_rect.bottom > screen_rect.bottom:
            status = True
        else:
            status = False
        return status

    def random_moving(self, sprite_group):
        self.erase()
        direction_list = ["up", "down", "left", "right"]
        random_direction = randint(0, 3)
        move_func = eval(f"self.move_{direction_list[self.__last_moving_direction]}")
        status = move_func(sprite_group)
        if status:
            self.__last_moving_direction = random_direction
