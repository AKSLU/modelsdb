import sqlite3 as sql

def create_table():
    conn = sql.connect("base.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            password TEXT,
            user_group TEXT
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS admins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()


