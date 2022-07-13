class Figure:
    def __init__(self, area=None):
        self.area = area
    
    def area(self):
        return NotImplementedError("В дочернем классе необходимо переопределить метод area")
    
    def perimeter(self):
        return NotImplementedError("В дочернем классе необходимо переопределить метод perimeter")
    
    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise ValueError('Передана не фигура')
