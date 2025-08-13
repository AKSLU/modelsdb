import sqlite3 as sql

def filtered_context():
    try:
        conn = sql.connect("base.db")
        cur = conn.cursor()

        cur.execute("SELECT login, password FROM users WHERE user_group = 'admin'")
        admin = cur.fetchall()

        cur.execute("SELECT login, password FROM users WHERE user_group = 'texpoderzka'")
        texpoderzka = cur.fetchall()

        cur.execute("SELECT login, password FROM users WHERE user_group = 'worker'")
        worker = cur.fetchall()

        return {
            'admin': admin,
            'texpoderzka': texpoderzka,
            'worker': worker
        }

    except Exception as e:
        print(f"Error in filtered_context: {e}")
        return {}

    finally:
        conn.close()

  
