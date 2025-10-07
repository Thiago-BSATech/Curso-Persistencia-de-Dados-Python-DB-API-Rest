import sqlite3

conn = sqlite3.connect("escola_db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

cursor.execute(
    "INSERT INTO estudantes (nome, idade)\
    VALUES (?, ?)", ("João", 20)
)
conn.commit()

cursor.execute("SELECT * FROM estudantes")

print(cursor.fetchall())

conn.close()

# é preciso o uso de DOCKER