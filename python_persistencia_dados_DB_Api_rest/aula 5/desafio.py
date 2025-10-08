import sqlite3

conn = sqlite3.connect("techmais_db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
""")





def criar_produto(nome, preco):
    cursor.execute("INSERT INTO products(name, price)\
                   VALUES(?, ?)", (nome, preco))
    conn.commit()

def listar_produtos():
    cursor.execute("SELECT * FROM products")
    response = cursor.fetchall()
    return response

# -- EXECUÇÃO --
criar_produto("p1", 2.0)
criar_produto("p2", 3.0)
criar_produto("p3", 4.0)
print(listar_produtos())