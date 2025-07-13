"""
Домашнее задание — Блок 2

ИНСТРУКЦИЯ ПО СДАЧЕ:
1. Создайте новую ветку с названием `homework11`
2. Добавьте этот файл и закоммитьте изменения в эту ветку
3. Создайте Pull Request в ветку `develop`

НЕ ПИШИТЕ РЕШЕНИЯ В КОММЕНТАРИЯХ! Используйте `# TODO` для пометок, где писать код.
"""

# === 1. Класс Soda ===
"""
ЗАДАНИЕ:
Создайте класс Soda. У него есть параметр — вкус (flavor).
Он может быть задан при инициализации, а может и не быть.
Реализуйте метод __str__, который возвращает:
- «У вас газировка с <вкусом> вкусом» — если вкус задан
- «У вас обычная газировка» — если вкус не задан
"""

class Soda:
    def __init__(self, flavor=None):
        # TODO: сохранить вкус, если он задан
        self.flavor = flavor
        

    def __str__(self):
        # TODO: реализовать строковое представление
        if self.flavor != None:
            return f'У вас газировка с {self.flavor} вкусом'
        else:
            return "У вас обычная газировка"
        
        


def test_soda():
    print(str(Soda("вишневым")))  # У вас газировка с вишневым вкусом
    print(str(Soda()))            # У вас обычная газировка


# === 2. Класс Math ===
"""
ЗАДАНИЕ:
Создайте класс Math. При инициализации он не принимает аргументов.
Добавьте методы:
- addition(a, b) — сложение
- subtraction(a, b) — вычитание
- multiplication(a, b) — умножение
- division(a, b) — деление
Каждый метод должен печатать результат.
"""

class Math:
    def addition(self, a, b):
        self.a = a
        self.b = b
        print(self.a + self.b)

    def subtraction(self, a, b):
        self.a = a
        self.b = b
        print(self.a - self.b)

    def multiplication(self, a, b):
        self.a = a
        self.b = b
        print(self.a * self.b)

    def division(self, a, b):
        self.a = a
        self.b = b
        if b == 0:
            print('Error, ZeroDivision')
        else:
            print(self.a / self.b)


def test_math():
    math = Math()
    math.addition(10, 5)        # 15
    math.subtraction(10, 5)     # 5
    math.multiplication(10, 5)  # 50
    math.division(10, 5)        # 2.0


# === 3. Класс Car ===
"""
ЗАДАНИЕ:
Создайте класс Car с атрибутами: color, type, year
Реализуйте методы:
- start() — печатает "Автомобиль заведён"
- stop() — печатает "Автомобиль заглушен"
- set_color(color) — задать цвет
- set_type(type) — задать тип
- set_year(year) — задать год выпуска
"""

class Car:
    def __init__(self, color, type_, year):
        self.color = color
        self.type_ = type_
        self.year = year
    
    def start(self):
        print('The car is started')

    def stop(self):
        print("The car is turned off")

    def set_year(self, year):
        self.year = year
        print(f"car year changed on {self.year}")

    def set_type(self, type_):
        self.type_ = type_
        print(f"type of car changed on {self.type_}")

    def set_color(self, color):
        self.color = color
        print(f"car color changed on {self.color}")


def test_car():
    car = Car("black", "sedan", 2020)
    car.start()
    car.stop()
    car.set_year(2022)
    car.set_color("red")
    car.set_type("SUV")


# === 4. Класс Sphere ===
"""
ЗАДАНИЕ:
Создайте класс Sphere с параметрами:
- radius (по умолчанию 1)
- координаты центра (x, y, z), по умолчанию (0, 0, 0)

Методы:
- get_volume() — возвращает объём
- get_square() — возвращает площадь поверхности
- get_radius() — возвращает радиус
- get_center() — возвращает координаты центра
- set_radius(r) — задаёт новый радиус
- set_center(x, y, z) — задаёт новый центр
- is_point_inside(x, y, z) — возвращает True, если точка внутри сферы
"""

import math

class Sphere:
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return(self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def is_point_inside(self, x, y, z):
        
        return ((x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2) <= self.radius ** 2


def test_sphere():
    s = Sphere(3, 1, 2, 3)
    print(s.get_radius())        # 3
    print(s.get_center())        # (1, 2, 3)
    print(round(s.get_volume(), 2))  # ~113.1
    print(round(s.get_square(), 2))  # ~113.1
    print(s.is_point_inside(1, 2, 3))      # True
    print(s.is_point_inside(100, 100, 100))  # False


# === 5. Класс SuperStr ===
"""
ЗАДАНИЕ:
Создайте класс SuperStr (наследуется от str)

Добавьте методы:
- is_repeatance(s): True, если строка состоит из целого числа повторов строки `s`
  Пример: "abcabc" -> is_repeatance("abc") → True
- is_palindrom(): True, если строка палиндром (без учёта регистра)
  Пример: "RaceCar" → True, "" → True
"""

class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str) or not s:
            return False
        if len(self) % len(s) != 0:
            return False
        repeat = len(self) // len(s)
        return self == s * repeat
    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]


def test_superstr():
    s = SuperStr("abcabc")
    print(s.is_repeatance("abc"))     # True
    print(s.is_repeatance("ab"))      # False
    print(s.is_repeatance(""))        # False
    print(SuperStr("RaceCar").is_palindrom())  # True
    print(SuperStr("hello").is_palindrom())    # False
    print(SuperStr("").is_palindrom())         # True


# === Запуск всех тестов ===

if __name__ == "__main__":
    print("=== Soda ===")
    test_soda()
    print("\n=== Math ===")
    test_math()
    print("\n=== Car ===")
    test_car()
    print("\n=== Sphere ===")
    test_sphere()
    print("\n=== SuperStr ===")
    test_superstr()