from .base_sprite import BaseCharacter


class BasicMonster(BaseCharacter):
    def __init__(self, speed, height, width, image, screen, background,
                 initial_position: tuple, *group):
        super(BasicMonster, self).__init__(speed, height, width, image, screen, background,
                                           initial_position, *group)
        self.health = 100

    def move_up(self, sprite_group):
        self._sprite_rect.centery -= self.speed
        self.stop_moving_out_screen()
        self.stop_across_obstacle_up(sprite_group)

    def move_down(self, sprite_group):
        self._sprite_rect.centerx += self.speed
        self.stop_moving_out_screen()
        self.stop_across_obstacle_down(sprite_group)

    def move_left(self, sprite_group):
        self._sprite_rect.centerx -= self.speed
        self.stop_moving_out_screen()
        self.stop_across_obstacle_left(sprite_group)

    def move_right(self, sprite_group):
        self._sprite_rect.centerx += self.speed
        self.stop_moving_out_screen()
        self.stop_across_obstacle_right(sprite_group)
