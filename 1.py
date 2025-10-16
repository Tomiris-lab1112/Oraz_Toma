import re

# Шаблон: 'a' + ноль или более 'b'
pattern = r'ab*'

# Примеры строк
test_strings = ["a", "ab", "abb", "ac", "b", "aaabbb"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Совпадение найдено: {s}")
    else:
        print(f"Нет совпадения: {s}")
