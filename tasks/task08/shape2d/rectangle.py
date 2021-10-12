from tasks.task08.shape2d.shape import *


class Rectangle(Shape):
    bottom_left = Point(0, 0)
    width = 0
    length = 0

    def __init__(self, bottom_left: Point, width: float, length: float):
        self.bottom_left = bottom_left
        self.width = width
        self.length = length

    def __contains_by_x(self, x: float) -> bool:
        return self.bottom_left.x <= x <= self.bottom_left.x + self.length

    def __contains_by_y(self, y: float) -> bool:
        return self.bottom_left.y - self.width <= y <= self.bottom_left.y

    def __contains__(self, point: Point) -> bool:
        return self.__contains_by_x(point.x) and self.__contains_by_y(point.y)

    def __str__(self) -> str:
        return f"Bottom left[x: {self.bottom_left.x}, y: {self.bottom_left.y}], Width: {self.width}, Length: {self.length}"

    def area(self) -> float:
        return self.width * self.length
