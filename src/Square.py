from src.Figure import Figure


class Square(Figure):
    def __init__(self, side=None):
        if side is None:
            raise ValueError("Не задана сторона квадрата")
        else:
            self.name = "Квадрат"
            self.side = side
    
    @property
    def area(self):
        return self.side ** 2
    
    @property
    def perimeter(self):
        return self.side * 4
