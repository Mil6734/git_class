import sqlite3

with sqlite3.connect('users.db') as con:
    cur = con.cursor()

    # cur.execute("""CREATE TABLE IF NOT EXISTS person(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     phone BLOB NOT NULL DEFAULT '+7909000000',
    #     age INTEGER CHECK(age > 0 AND age < 100),
    #     email TEXT UNIQUE
    # )""")
    #
    # cur.execute("""
    # ALTER TABLE person
    # RENAME TO person_table        # ПЕРЕИМЕНОВАНИЕ ТАБЛИЦЫ
    # """)
    #
    # cur.execute("""
    # ALTER TABLE person_table      #  ДОБАВЛЕНИЕ НОВОЙ КОЛОНКИ
    # ADD COLUMN address TEXT NOT NULL DEFAULT 'city, address'
    # """)
    #
    # cur.execute("""
    # ALTER TABLE person_table     #  ПЕРЕИМЕНОВАНИЕ КОЛОНКИ
    # RENAME COLUMN address TO nome_address
    # """)
    #
    # cur.execute("""
    # ALTER TABLE person_table    #  УДАЛЕНИЕ КОЛОНКИ
    # DROP COLUMN nome_address
    # """)
    #
    # cur.execute("""
    # DROP TABLE person_table       #   УДАЛЕНИЕ ТАБЛИЦЫ
    # """)