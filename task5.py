import sqlite3
import math

def fetch_weight_values():
    conn = sqlite3.connect('materials.db')
    cursor = conn.cursor()
    query = '''SELECT weight FROM materials'''
    cursor.execute(query)
    weight_values = [row[0] for row in cursor.fetchall()]
    conn.close()
    return weight_values

def calculate_average_and_round(weight_values):
    if not weight_values:
        return None
    total_weight = sum(weight_values)
    avg = total_weight / len(weight_values)
    return round(avg)

weight_values = fetch_weight_values()
average_weight = calculate_average_and_round(weight_values)

if average_weight is not None:
    print("Середнє значення ваги всіх матеріалів (округлене до цілого):", average_weight)
else:
    print("Список ваг не містить жодного значення.")
