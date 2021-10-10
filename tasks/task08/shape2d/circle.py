from tasks.task08.shape2d.shape import *
import math


class Circle(Shape):
    center = 0
    radius = 0

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def __contains__(self, point: Point) -> bool:
        return (point.x - self.center.x)**2 + (point.y - self.center.y)**2 <= self.radius**2

    def __str__(self) -> str:
        return f"Center: [x: {self.center.x}, y: {self.center.y}], Radius: {self.radius}"
