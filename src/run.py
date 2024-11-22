from figure import (
    Square,
    Circle
)


def client_code():
    # Создаем оригинальные фигуры
    circle = Circle(5)
    square = Square(10)
    # Создание клонов
    clone_circle = circle.copy()
    clone_square = square.copy()

    clone_circle.radius = 10 #Изменяем радиус у клонированного круга
    
    print(circle)
    print(square)
    print(clone_circle)
    print(clone_square)

client_code()