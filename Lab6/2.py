#Python Directories and Files exercises
#1.Вывод директорий, файлов и всех элементов в указанном пути
"Показывает только директории (папки)"
"Показывает только файлы"
"Показывает все элементы (файлы и директории)"
"модуль os"

import os

def list_path_contents(path):
    if not os.path.exists(path):
        print(f"Путь '{path}' не существует.")
        return

    items = os.listdir(path)

    print("\nТолько директории:")
    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            print(" -", item)

    print("\nТолько файлы:")
    for item in items:
        if os.path.isfile(os.path.join(path, item)):
            print(" -", item)

    print("\nВсе элементы:")
    for item in items:
        print(" -", item)

# Запрос пути у пользователя
user_path = input("Введите путь: ")
list_path_contents(user_path)
