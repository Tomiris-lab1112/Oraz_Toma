#Python Math library
#1. Конвертация градусов в радианы:
import math
degree = float(input("Input degree: "))    #Ввод значения в градусах
radian = math.radians(degree)    #Переводим градусы в радианы
print(f"Output radian: {radian:.6f}")   #Выводим результат с 6 знаками после запятой
 
"Пример работы: "
"Input degree: 15 "
"Output radian: 0.261799 "


#2. Вычисляет площадь трапеции:
height = float(input("Height: "))    #Ввод исходных данных
base_1 = float(input("Base, first value: "))  
base_2 = float(input("Base, second value: "))
area = ((base_1 + base_2) / 2) * height    #Формула площади трапеции: S = ((a + b) / 2) * h
print(f"Expected Output: {area}")

"Пример работы:"
"Height: 5 "
"Base, first value: 5"
"Base, second value: 6"
"Expected Output: 27.5"


#3. Вычисляет площадь правильного многоугольника:
import math
num_sides = int(input("Input number of sides: "))    # Ввод данных
side_length = float(input("Input the length of a side: "))
area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))   #Формула площади правильного многоугольника:
# S = (n * a^2) / (4 * tan(pi / n))
print(f"The area of the polygon is: {area:.0f}")

"Пример работы:"
"Input number of sides: 4"
"Input the length of a side: 25"
"The area of the polygon is: 625"


#4. Вычисляет площадь параллелограмма: 

base = float(input("Length of base: "))    #Ввод исходных данных
height = float(input("Height of parallelogram: "))
area = base * height   #Формула площади параллелограмма: S = base * height
print(f"Expected Output: {area:.1f}")

"Пример работы:"
"Length of base: 5"
"Height of parallelogram: 6"
"Expected Output: 30.0"
