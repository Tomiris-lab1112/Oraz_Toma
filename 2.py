#Python date
#1. Вычесть 5 дней из текущей даты
from datetime import datetime, timedelta
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("Сегодня:", today)
print("5 дней назад:", five_days_ago)


#2. Вывести вчерашнюю, сегодняшнюю и завтрашнюю дату
from datetime import datetime, timedelta
today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Вчера:", yesterday)
print("Сегодня:", today)
print("Завтра:", tomorrow)


#3. Удалить микросекунды из объекта datetime
from datetime import datetime
now = datetime.now()
without_microseconds = now.replace(microsecond=0)
print("Оригинальная дата/время:", now)
print("Без микросекунд:", without_microseconds)


#4. Вычислить разницу между двумя датами в секундах

from datetime import datetime
# Пример: задаём вручную две даты
date1 = datetime(2025, 10, 6, 12, 0, 0)
date2 = datetime(2025, 10, 6, 12, 1, 30)
difference = abs((date2 - date1).total_seconds())
print("Разница в секундах:", difference)

"total_seconds() — возвращает разницу между датами в секундах (в виде числа с плавающей точкой)."