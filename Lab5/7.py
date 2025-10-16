#которая преобразует строку в snake_case в camelCase.

# Программа, которая преобразует строку из snake_case в camelCase

def snake_to_camel(snake_str):
    # Разбиваем строку по символу '_'
    parts = snake_str.split('_')
    # Первый элемент оставляем как есть, остальные начинаются с заглавной буквы
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

# Пример использования
snake_str = "this_is_snake_case"
camel_case = snake_to_camel(snake_str)

print("Исходная строка:", snake_str)
print("Преобразованная строка (camelCase):", camel_case)

 

 #Кратко объяснение:

#split('_') — разбивает строку по символу подчёркивания.
#Первый элемент остаётся как есть (нижний регистр).
#Остальные слова превращаем в заглавную букву + остальное в нижнем регистре (capitalize()).
#Склеиваем обратно в одну строку.

#split('_') → разбивает строку "this_is_snake_case" на список ["this", "is", "snake", "case"].
#Первый элемент "this" остаётся без изменений.
#Остальные ("is", "snake", "case") становятся "Is", "Snake", "Case".
#Склеиваем всё: "thisIsSnakeCase".