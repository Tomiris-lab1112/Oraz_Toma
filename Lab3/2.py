#Python Function
#1. Перевод граммов в унции 
'''
Задача: рецепт написан в граммах, а магазин продаёт продукты в унциях. 
Нужно перевести граммы в унции.
'''
#Формула: унции = 28.3495231 * граммы 
def grams_to_ounces(grams):
    return 28.3495231 * grams

# пример
print(grams_to_ounces(10))  # 283.495231

#Мы создали функцию, которая принимает граммы и возвращает результат в унциях.


#2. Перевод температуры Фаренгейта в Цельсий
'''
Берём температуру в Фаренгейтах, применяем формулу и получаем температуру в Цельсиях.
'''
# Формула: С = ( 5 / 9 ) * ( F - 32 )
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

#пример
print(fahrenheit_to_celsius(100))  # 37.777...


#3. Классическая задача про кур и кроликов
'''
У нас на ферме 35 голов и 94 ноги. Сколько кур и кроликов?
• У курицы: 1 голова и 2 ноги
• У кролика: 1 голова и 4 ноги\
'''
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):  # пробуем все варианты кур
        rabbits = numheads - chickens     # оставшиеся головы – это кролики
        if 2 * chickens + 4 * rabbits == numlegs:  # проверяем количество ног
            return chickens, rabbits
    return None  # если решения нет
#пример
print(solve(35, 94))  # (23, 12)
#Мы перебираем количество кур, вычисляем сколько кроликов остаётся,проверяем совпадают ли ноги. Ответ: 23 курицы и 12 кроликов.


#4. Фильтрация простых чисел
'''
Простое число — делится только на 1 и на себя.
• Сначала пишем функцию is_prime, чтобы проверить число.
• Потом фильтруем список и оставляем только простые числа.
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]
# пример
print(filter_prime([1, 2, 3, 4, 5, 11, 15]))  # [2, 3, 5, 11]


#5. Все перестановки строки
'''
Нужно вывести все возможные комбинации символов строки. String
Используем готовую функцию permutations из itertools, 
чтобы получить все перестановки символов.
'''
from itertools import permutations

def string_permutations(s):
    perms = permutations(s)
    for p in perms:
        print("".join(p))
# пример
string_permutations("abc")


#6. Переворот слов в предложении
'''
Пример: 
Вход: "We are ready"
Выход: "ready are We"

Мы разбиваем строку на список слов,
меняем их порядок на обратный и соединяем обратно в предложение.
'''
def reverse_sentence(sentence):
    words = sentence.split()     # разбиваем строку на слова
    return " ".join(words[::-1]) # переворачиваем список слов

# пример
print(reverse_sentence("We are ready"))  # ready are We


#7. Есть ли в списке два 3 подряд
'''
Мы идём по списку и смотрим, есть ли где-то подряд два числа 3.
'''
def has_33(nums):
    for i in range(len(nums) - 1):   # идем по списку до предпоследнего элемента
        if nums[i] == 3 and nums[i + 1] == 3:  # проверяем два подряд
            return True
    return False

# Примеры
print(has_33([1, 3, 3]))      # True
print(has_33([1, 3, 1, 3]))   # False
print(has_33([3, 1, 3]))      # False


#8. 