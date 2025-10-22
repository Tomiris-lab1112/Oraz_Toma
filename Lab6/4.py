#3. Проверка существования пути и выделение файла и директории
"Проверяет, существует ли указанный путь"
"Если существует, выводит:"
"Директорию (путь к папке)"
"Имя файла"

import os

def check_path(path):
    if os.path.exists(path):
        print(f"\n Путь существует: {path}")

        directory = os.path.dirname(path)
        filename = os.path.basename(path)

        print("Путь к директории:", directory)
        print("Имя файла:", filename)
    else:
        print(f"\n Путь НЕ существует: {path}")

# Запрос пути у пользователя
user_input = input("Введите путь для проверки: ")
check_path(user_input)
