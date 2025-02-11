# Описание паттерна

__*Паттерн Прототип (Prototype)*__ — это порождающий паттерн проектирования, который позволяет создавать новые объекты на основе существующих, используя их в качестве шаблонов. Этот паттерн используется для копирования объектов, а не их создания с нуля, что может быть полезно, когда создание нового экземпляра объекта является более затратным по времени или ресурсам.

# Цель паттерна
Целью паттерна Прототип является:

- Упрощение создания объектов путем копирования существующих.

- Снижение зависимости от конкретных классов и облегчение управления объектами.

- Устранение необходимости в сложных конструкторах инициализации.


# _Проблема, которую решает паттерн_
Паттерн Прототип решает проблему создания объектов, когда:

1. Создание нового объекта требует значительных затрат ресурсов (времени или памяти).

2. Необходимо создать множество объектов с похожими 
   характеристиками.
3. Сложные инициализации объектов могут быть упрощены путем копирования существующих объектов.


# Когда использовать паттерн
Паттерн __Прототип__ рекомендуется использовать в следующих случаях:

- Когда классы имеют много общего состояния и поведения, и создание новых экземпляров требует больших затрат.

- Когда необходимо динамически изменять объекты во время выполнения.

- Когда нужно создавать множество однотипных объектов, но с небольшими изменениями.

# Пример кода на Python
Рассмотрим пример реализации паттерна Прототип на основе системы управления графическими фигурами.
1. Определим интерфейс прототипа

```python
import copy

class Shape:
    
    def clone(self):
        pass

```

2. Создадим конкретные прототипы
```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Square with side length: {self.side_length}"
```

3. Создадим клиентский код

Клиентский код будет использовать прототипы для создания новых фигур.
```python
def client_code():
    # Создаем оригинальные фигуры
    circle = Circle(5)
    square = Square(4)

    # Клонируем фигуры
    circle_clone = circle.clone()
    square_clone = square.clone()

    # Изменяем радиус у клонированного круга
    circle_clone.radius = 10

    # Выводим информацию о фигурах
    print(circle)         # Circle with radius: 5
    print(circle_clone)   # Circle with radius: 10
    print(square)         # Square with side length: 4
    print(square_clone)   # Square with side length: 4

# Запуск клиентского кода
client_code()

```



# Взаимодействие классов и методов

- Интерфейс Shape определяет метод `clone()`, который должен реализовываться всеми конкретными фигурами.

- Классы Circle и Square реализуют интерфейс Shape и предоставляют свою реализацию метода `clone()`, используя copy.deepcopy() для создания глубоких копий объектов.

- Клиентский код создает оригинальные объекты фигур и использует метод `clone()` для создания их копий. Изменения в клонированных объектах не влияют на оригиналы.


# Краткое описание проекта
В данном проекте реализована система управления графическими фигурами с использованием паттерна Прототип. Система позволяет создавать новые экземпляры фигур (кругов и квадратов) путем клонирования существующих объектов. Это упрощает процесс создания фигур и позволяет избежать затрат на повторную инициализацию.

# Заключение
Паттерн Прототип предоставляет мощный механизм для создания новых объектов путем копирования существующих. Он помогает упростить процесс создания объектов, особенно когда речь идет о сложных или ресурсоемких объектах. Использование этого паттерна позволяет избежать избыточности кода и улучшить производительность системы.
