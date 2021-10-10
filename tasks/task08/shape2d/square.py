from tasks.task08.shape2d.rectangle import *


class Square(Rectangle):
    def __init__(self, bottom_left: Point, width: float):
        super().__init__(bottom_left, width, width)
