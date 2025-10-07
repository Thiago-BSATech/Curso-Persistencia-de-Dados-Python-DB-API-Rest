import sqlite3 


conn = sqlite3.connect("hotelplus_db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT                             
)

""")

continue_while_bool = True

while continue_while_bool:
    new_user_name = input("Digite seu nome: \n")
    new_user_email = input("Digite seu email: \n")

    cursor.execute(
        "INSERT INTO users (name, email)\
        VALUES (?, ?)", (new_user_name, new_user_email)
    )
    conn.commit()


    continue_while = input("QUER ADICIONAR MAIS UM? (Y: SIM | N: NÃO) : \n")

    if(continue_while == "N"):

        continue_while_bool = False

        cursor.execute("SELECT * FROM users")

        print(cursor.fetchall())
    else:
        continue