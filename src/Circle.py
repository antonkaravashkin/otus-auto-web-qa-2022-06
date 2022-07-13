from src.Figure import Figure
import math


class Circle(Figure):
    def __init__(self, radius=None):
        if radius is None:
            raise ValueError("Не задан радиус круга")
        self.name = "Круг"
        self.radius = radius
    
    @property
    def area(self):
        return int(math.pi * (self.radius ** 2))
    
    @property
    def perimeter(self):
        return int(2 * math.pi * self.radius)
