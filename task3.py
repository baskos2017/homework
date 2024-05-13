import csv

# Створення власного діалекту
my_dialect = csv.Dialect
my_dialect.delimiter = '|'
my_dialect.quotechar = '"'
my_dialect.quoting = csv.QUOTE_MINIMAL
my_dialect.lineterminator = '\n'

# Зареєструвати створений діалект
csv.register_dialect('my_dialect', my_dialect)

# Записати дані у файл з використанням створеного діалекту
with open('baskos.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='my_dialect')
    writer.writerow(['Name', 'Age', 'Phone'])
    writer.writerow(['Vasya', '30', '123456789'])
    writer.writerow(['Vova', '25', '987654321'])

# Читання даних з файлу з використанням створеного діалекту
with open('data.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, dialect='my_dialect')
    for row in reader:
        print(row)
