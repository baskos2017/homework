import sqlite3

def concatenate_fields_from_materials(*fields):
    conn = sqlite3.connect('materials.db')
    cursor = conn.cursor()

    fields_str = ', '.join(fields)

    query = f'''SELECT {fields_str} FROM materials'''
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()

    concatenated_values = []
    for row in rows:
        concatenated_values.append(' '.join(map(str, row)))
    return concatenated_values

concatenated_values = concatenate_fields_from_materials('weight', 'height', 'extra_attributes')
for value in concatenated_values:
    print(value)
