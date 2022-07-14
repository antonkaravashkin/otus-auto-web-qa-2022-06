from src.Figure import Figure
import math


class Triangle(Figure):
    def __new__(cls, *args):
        if None in args:
            raise ValueError('Треугольник задается тремя сторонами')
    
    def __init__(self, side1=None, side2=None, side3=None):
        self.name = "Треугольник"
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    @property
    def area(self):
        p = self.perimeter / 2
        return int(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)))
    
    @property
    def perimeter(self):
        return int((self.side1 + self.side2 + self.side3))
