import sqlite3

people = [
    ('Андрей', 'Смоленск', 18),
    ('Алексей', 'Москва', 19),
    ('Юрий', 'Краснодар', 20),
    ('Наталья', 'Казань', 21)
]

with sqlite3.connect("people.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS people(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        city TEXT,
        age INTEGER
        )
    """)
for i in people:
    cur.execute('INSERT INTO people VALUES (NULL, ?, ?, ?)', i)
con.commit()
con.close()
