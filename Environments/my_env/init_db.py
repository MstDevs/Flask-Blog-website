import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content,tags) VALUES (?, ?, ?)",
            ('Holiday Post', 'A trip along the coast with mates','#holiday,#Summer,#beach')
	    )
cur.execute("INSERT INTO posts (title, content,tags) VALUES (?, ?, ?)",
            ('Second Post', 'Content for the second post','#try,#testing,#nje')
            )

connection.commit()
connection.close()
