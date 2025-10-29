#4. Которая считает количество строк в файле.

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Количество строк: {len(lines)}")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запрос пути к файлу у пользователя
path = input("Введите путь к текстовому файлу: ")
count_lines(path)
