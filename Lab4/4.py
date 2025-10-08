#Python JSON parsing
#json это текстовый формат хранения данных, название расшифровывается как: JavaScript Object Notation

import json

# Открываем и читаем JSON-файл
with open("sample-data.json") as f:
    data = json.load(f)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

# Извлекаем нужные данные
# В sample-data.json структура обычно такая:
# data["imdata"] — список словарей, в каждом есть ключ "l1PhysIf"
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")
