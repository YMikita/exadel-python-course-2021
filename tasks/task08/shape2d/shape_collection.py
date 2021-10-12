from tasks.task08.shape2d.shape import *


class ShapeCollection(Shape):
    __stores: list[Shape] = []

    def __init__(self, stores: list[Shape]):
        self.__stores = stores

    def area(self) -> float:
        sum_area: float = 0
        for shape in self.__stores:
            sum_area += shape.area()
        return sum_area

    def __str__(self) -> str:
        all_str: str = ""
        for shape in self.__stores:
            all_str += shape.__str__() + "\n"
        return all_str

    def __contains__(self, point: Point) -> bool:
        for shape in self.__stores:
            if shape.__contains__(point):
                return True
        return False
