import sqlite3 as sql

class Users:
    def __init__(self, login, password, group, id_=None):
        self.login = login
        self.password = password
        self.group = group
        self.id = id_

    def save(self):
        try:
            conn = sql.connect("base.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO users(login, password, user_group) VALUES (?, ?, ?)",
                        (self.login, self.password, self.group))
            conn.commit()
            print("User saved")
        except Exception as e:
            print(f"Error saving user: {e}")
        finally:
            conn.close()

    @staticmethod
    def all_users():
        try:
            conn = sql.connect("base.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            return users
        except Exception as e:
            print(f"Error fetching all users: {e}")
        finally:
            conn.close()


class Admin:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def save(self):
        try:
            conn = sql.connect("base.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO admins(login, password) VALUES (?, ?)",
                        (self.login, self.password))
            conn.commit()
            print("Admin saved")
        except Exception as e:
            print(f"Error saving admin: {e}")
        finally:
            conn.close()

    @staticmethod
    def group_admin():
        try:
            conn = sql.connect("base.db")
            cur = conn.cursor()
            cur.execute("SELECT login, password FROM users WHERE user_group = 'admin'")
            admins = cur.fetchall()
            for i in admins:
                cur.execute("INSERT OR IGNORE INTO admins(login, password) VALUES (?, ?)", i)
            conn.commit()
        except Exception as e:
            print(f"Error in group_admin: {e}")
        finally:
            conn.close()


      
