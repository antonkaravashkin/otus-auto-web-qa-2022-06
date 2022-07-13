import pytest


from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from data.geom_data import TRIANGLE, SQUARE, CIRCLE, RECTANGLE


@pytest.fixture(scope="session")
def triangle_creation():
    triangle = Triangle(*TRIANGLE)
    yield triangle
    del triangle


@pytest.fixture(scope="session")
def square_creation():
    square = Square(SQUARE)
    yield square
    del square


@pytest.fixture(scope="session")
def circle_creation():
    circle = Circle(CIRCLE)
    yield circle
    del circle


@pytest.fixture(scope="session")
def rectangle_creation():
    rectangle = Rectangle(*RECTANGLE)
    yield rectangle
    del rectangle
