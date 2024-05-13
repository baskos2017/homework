import json

data = {
    'Один': 1,
    'Два': 2,
    'Три': 3,
    'Чотири': 4,
    'П`ять': 5,
    'Шість': 6,
    'Сім': 7,
    'Вісім': 8,
    'Дев`ять': 9,
    'Десять': 10
    
 
 }

json_data = json.dumps(data, ensure_ascii=False)
print(json_data)

with open('my_output.json', 'w') as f:
    json.dump(data, f)

with open('my_output.json', 'r') as f:
    my_data= json.load(f)

print('Дані з файлу:\n', my_data)
