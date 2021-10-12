from tasks.task08.shape2d.square import *
from tasks.task08.shape2d.shape_collection import *
from tasks.task08.shape2d.circle import *

point = Point(50, 70)
point2 = Point(60, 60)
rectangle = Rectangle(point, 10, 20)
print(f"Rectangle: {rectangle}, Area: {rectangle.area()}, Point[{point2}] contains: {rectangle.__contains__(point2)}")

square = Square(point, 30)
print(f"Square: {square}, Area: {square.area()}, Point[{point2}] contains: {square.__contains__(point2)}")

circle = Circle(point, 15)
print(f"Circle: {circle}, Area: {circle.area()}, Point[{point2}] contains: {circle.__contains__(point2)}")

shape_collection = ShapeCollection([rectangle, square, circle])
print(f"\nPoint[{point2}] contains in Shape Collection: {shape_collection.__contains__(point2)}")
print(f"Shape Collection Area: {shape_collection.area()}")
print(f"Shape Collection: {shape_collection}")
