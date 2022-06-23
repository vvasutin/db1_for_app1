import sqlite3

connection = sqlite3.connect('database.db')


with open('dbshem.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Pervaya citata', 'Avtor, kniga')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Vtoraya citata', 'Avtor, vtoraya kniga')
            )

connection.commit()
connection.close()
