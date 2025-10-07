import sqlite3 
from faker import Faker


conn = sqlite3.connect("hotelplus_leo_db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT                             
)
""")



# DESAFIO DE LEO -->
fake = Faker('pt_BR')

continue_while_not_500 = 0
continue_while_bool = True

while continue_while_bool:

    new_user_name = fake.name()
    new_user_email = fake.email()

    cursor.execute(
        "INSERT INTO users (name, email)\
        VALUES (?, ?)", (new_user_name, new_user_email)
    )
    
    conn.commit()
    continue_while_not_500 += 1

    if(continue_while_not_500 >= 500):

        continue_while_bool = False

        cursor.execute("SELECT * FROM users")

        print(cursor.fetchall())
    else:
        continue