import csv
import json
from xml.etree.ElementTree import Element, SubElement, tostring


def create_csv_file():
    rows = []
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    birth_date = input("Введіть дату народження (у форматі DD.MM.YYYY): ")
    city = input("Введіть місто проживання: ")
    rows.append([{name}, surname, birth_date, city])

    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Ім\'я', 'Прізвище', 'Дата народження', 'Місто проживання'])
        writer.writerows(rows)

def overwrite_csv_file():
    create_csv_file()
    
def append_to_csv_file():
   #create_csv_file()
    rows = []
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    birth_date = input("Введіть дату народження (у форматі DD.MM.YYYY): ")
    city = input("Введіть місто проживання: ")
    rows.append([name, surname, birth_date, city])
    with open('data.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def read_csv_file():
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))
            

def convert_to_xml():
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        root = Element('users')
        for row in reader:
            user = SubElement(root, 'user')
            name = SubElement(user, 'name')
            name.text = row[0]
            surname = SubElement(user, 'surname')
            surname.text = row[1]
            birth_date = SubElement(user, 'birth_date')
            birth_date.text = row[2]
            city = SubElement(user, 'city')
            city.text = row[3]
    
    xml_string = tostring(root, encoding='utf-8').decode()
    with open('data.xml', 'w', encoding='utf-8') as xml_f:
        xml_f.write(xml_string)

def convert_to_json():
    with open('data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append({'name': row[0], 'surname': row[1], 'birth_date': row[2], 'city': row[3]})
    
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, indent=4)

while True:


  user_select = int(input('1 - Додати користувача, 2 - Перезаписати файл, 3 - Додати новий рядок, 4 - Прочитати файл,  - Конвертація в XML, 6 - Конвертація в JSON 0 - exit\n\n'))

  if user_select == 1:
    create_csv_file()

  elif user_select == 2:
    overwrite_csv_file()

  elif user_select == 3:
    append_to_csv_file()

  elif user_select == 4:
    read_csv_file()

  elif user_select == 5:
   convert_to_xml()
  
  elif user_select == 6:
   convert_to_json()

  elif user_select == 0:
    break

