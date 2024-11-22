from interface import Shape
import copy


class Circle(Shape):
    """Круг

    Args:
        Shape (_type_): _description_

    Returns:
        _type_: _description_
    """
    def __init__(self,radius):
        self.radius = radius
    
    def copy(self):
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"Радиус круга {self.radius}"


class Square(Shape):
    """Квадрат

    Args:
        Shape (_type_): _description_
    """
    
    def __init__(self,side_lenght):
        self.side_lenght = side_lenght

    def copy(self):
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"Стороны квадрата {self.side_lenght}"