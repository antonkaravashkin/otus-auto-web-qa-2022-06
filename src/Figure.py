class Figure:
    def __init__(self, area=None):
        self.area = area
    
    @property
    def area(self) -> int:
        pass
    
    @property
    def perimeter(self) -> int:
        pass
    
    def add_area(self, other):
        if isinstance(other, Figure):
            return self.area + other.area
        else:
            raise ValueError('Передана не фигура')
