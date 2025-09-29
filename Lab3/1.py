#Задание 1:
#Класс с методами getString() и printString()
'''
Описание:
Создать класс, у которого есть как минимум два метода:
getString() — получает строку от пользователя с консоли.
printString() — выводит строку в верхнем регистре.
'''
class StringHandler:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print(self.input_string.upper())

#Задание 2: 
#Класс Shape и подкласс Square
'''
Описание:
Создать класс Shape с методом area(), который возвращает площадь = 0.
Создать подкласс Square, принимающий длину стороны при инициализации и вычисляющий площадь.
'''
class Shape:
    def area(self):
        print("Площадь:", 0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        площадь = self.length ** 2
        print("Площадь квадрата:", площадь)

#Задание 3:
# Класс Rectangle, наследующий Shape
'''
Описание:
Класс Rectangle наследует Shape.
Принимает длину и ширину при создании объекта.
Метод area() вычисляет площадь прямоугольника.
'''
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        площадь = self.length * self.width
        print("Площадь прямоугольника:", площадь)

#Задание 4:
#Класс Point
'''
Описание:
Создать класс Point, у которого есть:
Метод show() – выводит координаты точки.
Метод move(x, y) – изменяет координаты точки.
Метод dist(other_point) – считает расстояние между двумя точками (используя теорему Пифагора).
'''
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

#Задание 5:
#Класс Account
'''
Атрибуты:
owner — владелец счёта
balance — текущий баланс (по умолчанию 0)

Методы:
deposit(amount) — пополняет счёт на указанную сумму
withdraw(amount) — снимает сумму, если на счёте достаточно денег
если нет — выводит сообщение: "Недостаточно средств"
'''
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнение: +{amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма для пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снятие: -{amount}. Текущий баланс: {self.balance}")
        else:
            print("Недостаточно средств для снятия.")

    def show_balance(self):
        print(f"Баланс счета {self.owner}: {self.balance}")

#Задание 6 
#Использовать встроенную функцию filter().
#Использовать lambda для определения анонимной функции.

'''
Число больше 1, которое делится только на 1 и само на себя.
Например: 2, 3, 5, 7, 11, 13, 17, ...

is_prime(n) — обычная функция, проверяющая, простое ли число.
lambda x: is_prime(x) — лямбда-функция (анонимная), которую принимает filter.
filter() применяет её ко всем элементам списка и оставляет только те, где результат — True.

Решение: с filter() и lambda
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Пример списка
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 20]

# Фильтруем простые числа с помощью filter и lambda
primes = list(filter(lambda x: is_prime(x), numbers))
'''
Результат:
print("Простые числа в списке:", primes)

Простые числа в списке: [2, 3, 5, 7, 11, 13, 17]
'''
