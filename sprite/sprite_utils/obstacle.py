import pygame.surface
import pygame.sprite
from sprite.sprite_model.obstacle import BasicObstacle


class GeneratorObject:
    def __init__(self, object_iterator, last_object_position: tuple):
        """
        :param object_iterator:
        :param last_object_position: (top, left)
        """
        self.object_iterator = object_iterator
        self.type = type(object_iterator)
        self.length = len(object_iterator)
        self.last_object_position = last_object_position


def obstacles_generator(
        size: tuple,
        image: str,
        number: int,
        direction: str,
        initial_position: tuple,
        screen: pygame.surface.Surface,
        background: pygame.surface.Surface,
        existed_group: pygame.sprite.Group = None,
        offset: int = None
):
    """
    in order to create several obstacles
    :param size: (height, width)
    :param image: path of the image
    :param number: how many obstacles you want to create
    :param direction: in which direction you want to create them, such as left, right, up, down
    :param initial_position: (top, left)
    :param screen: a pygame Surface type object
    :param background: a pygame Surface type object
    :param existed_group: in case you want to add the obstacles to a existed pygame group
    :param offset: in case there are some gaps between each object
    :return:
    """
    direction = direction.lower()
    obstacle_list = list()
    last_object_top_position, last_object_left_position = int(), int()
    top_, left_ = initial_position[0], initial_position[1]
    for i in range(0, number):
        basic_obstacle = BasicObstacle(size[0], size[1], image, screen, background, (left_, top_))
        if direction == "left":
            left_ = basic_obstacle.left - basic_obstacle.width
        elif direction == "right":
            left_ = basic_obstacle.right
        elif direction == "top":
            top_ = basic_obstacle.bottom - basic_obstacle.height
        elif direction == "down":
            top_ = basic_obstacle.bottom
        else:
            raise ValueError("please input a valid direction!")

        if i == number - 1:
            last_object_top_position, last_object_left_position = basic_obstacle.top, basic_obstacle.left

        existed_group.add(basic_obstacle)
        if not existed_group:
            obstacle_list.append(basic_obstacle)

    generator_object = GeneratorObject(
        existed_group if existed_group else obstacle_list,
        (last_object_top_position, last_object_left_position)
    )
    return generator_object
