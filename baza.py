import sqlite3

conn = sqlite3.connect("baza.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS logins (
               login TEXT PRIMARY KEY,
                password TEXT,
               name IEXT,
               amount INT,
               pin TEXT
)""")

# cursor.execute("""INSERT INTO logins VALUES (
#                'user',
#                '1234',
#                'Oleg',
#                '10000',
#                '123'
# ), (
#                'user2',
#                '4321',
#                'Patrick',
#                200,
#                'rrr'
# ) """)

# conn.commit()

def get_data(insert_login):
    cursor.execute("""SELECT * FROM logins WHERE login = (?)""", [insert_login])
    return cursor.fetchall()