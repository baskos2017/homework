import sqlite3

conn = sqlite3.connect('materials.db')
cursor = conn.cursor()

def create_materials_table():
    query = '''CREATE TABLE IF NOT EXISTS materials (
                    id INTEGER PRIMARY KEY,
                    weight REAL,
                    height REAL,
                    extra_attributes TEXT
                )'''


    cursor.execute(query)
    conn.commit()
    
def insert_materials():
    query = '''INSERT INTO materials (weight, height, extra_attributes) VALUES (10.5, 0.6, "[('Колір', 'Синій'), ('Тип', 'Метал')]")'''
    query1 = '''INSERT INTO materials (weight, height, extra_attributes) VALUES (12.8, 0.9, "[('Колір', 'Сірий'), ('Тип', 'Метал')]")'''
    cursor.execute(query)
    cursor.execute(query1)
    conn.commit()
    conn.close()

create_materials_table()
insert_materials()