#14. Импорт функций в другой файл
'''
Например, создаём два файла:

functions.py
(сюда помещаем весь код выше — задачи 1 - 13).

 main.py
(сюда пишем тесты и импорт):

тестовый файл, где ты запускаешь все функции, 
чтобы убедиться, что они работают правильно.
'''
from functions import grams_to_ounces, fahrenheit_to_celsius, solve, filter_prime, sphere_volume

print(grams_to_ounces(10))        # тест задачи 1
print(fahrenheit_to_celsius(100)) # тест задачи 2
print(solve(35, 94))              # тест задачи 3
print(filter_prime([1,2,3,4,5]))  # тест задачи 4
print(sphere_volume(3))           # тест задачи 9