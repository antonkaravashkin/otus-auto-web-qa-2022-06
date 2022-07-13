from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a=None, side_b=None):
        if None in [side_a, side_b]:
            raise ValueError('Прямоугольник задается двумя сторонами')
        else:
            self.name = "Прямоугольник"
            self.side_a = side_a
            self.side_b = side_b
    
    @property
    def area(self):
        return self.side_a * self.side_b
    
    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)
