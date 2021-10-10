import unittest
import math
from tasks.task08.shape2d.square import *
from tasks.task08.shape2d.circle import *


class TestRectangle(unittest.TestCase):
    __rectangle = Rectangle(Point(60, 60), 10, 20)

    def test_area(self):
        self.assertEqual(self.__rectangle.area(), 200)

    def test_contains(self):
        self.assertEqual(self.__rectangle.__contains__(Point(65, 55)), True)


class TestSquare(unittest.TestCase):
    __square = Square(Point(60, 60), 10)

    def test_area(self):
        self.assertEqual(self.__square.area(), 100)

    def test_contains(self):
        self.assertEqual(self.__square.__contains__(Point(55, 60)), False)


class TestCircle(unittest.TestCase):
    __circle = Circle(Point(60, 60), 10)

    def test_area(self):
        self.assertEqual(self.__circle.area(), math.pi*10**2)

    def test_contains(self):
        self.assertEqual(self.__circle.__contains__(Point(55, 52)), True)


if __name__ == '__main__':
    unittest.main()
