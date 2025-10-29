#Python Builtin functions exercises
#1. Builtin function to multiply all the numbers in a list
from functools import reduce
import operator
numbers = [2, 3, 4, 5]
result = reduce(operator.mul, numbers)
print("Произведение всех чисел:", result)

"reduce() — применяет функцию к элементам списка последовательно."
"operator.mul — обычное умножение (*) как функция."
"Результат: 2 * 3 * 4 * 5 = 120"


#2. Builtin function that accepts a string and calculate the number of upper case letters and lower case letters
#Подсчитать количество заглавных и строчных букв
def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())  # считаем заглавные
    lower = sum(1 for ch in s if ch.islower())  # считаем строчные
    print("Заглавных букв:", upper)
    print("Строчных букв:", lower)

text = input("Введите строку: ")
count_case(text)

"Проходит по каждому символу."
"Если символ заглавный - прибавляем 1."
"Если строчный - прибавляем 1 к другой переменной."
"Используем sum() — встроенную функцию для подсчёта."


#3. Builtin function that checks whether a passed string is palindrome or not.
#Проверить, является ли строка палиндромом
#Палиндром — это слово, которое читается одинаково слева направо и справа налево.
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # убираем пробелы и регистр
    return s == s[::-1]             # сравниваем строку с её обратной версией

word = input("Введите строку: ")
print("Палиндром?", is_palindrome(word))

"[:: -1]"
"Это срез, который переворачивает строку наоборот."


#4. invoke square root function after specific milliseconds
#Найти квадратный корень после заданного количества миллисекунд
import time
import math
number = int(input("Введите число: "))         # например 25100
milliseconds = int(input("Введите миллисекунды: "))  # например 2123
time.sleep(milliseconds / 1000)  # миллисекунды -> секунды
result = math.sqrt(number)
print(f"Квадратный корень из {number} через {milliseconds} миллисекунд = {result}")


#5. builtin function that returns True if all elements of the tuple are true.
#Проверить, что все элементы кортежа равны True
#Используем встроенную функцию all().
t = (True, True, True)
print(all(t))  # True, потому что все значения истинные

t2 = (True, False, True)
print(all(t2))  # False, потому что одно значение — False

"all(iterable) - возвращает True, если все элементы истинные."
"Если хотя бы один элемент равен False, результат будет False."