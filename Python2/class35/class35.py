import sqlite3

with sqlite3.connect('db_4.db') as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 5 OFFSET 2;
    """)

    # reg = cur.fetchall()
    # print(reg)

    # for res in cur:
    #     print(res)

    res = cur.fetchone()
    print(res)
