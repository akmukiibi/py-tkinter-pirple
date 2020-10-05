import sqlite3 as sql  # we wanna use a portable (file-based) database struct of sqlite


class Database:

    def __init__(self, db):
        """
        Create our database using DDL
        :param db:
        """
        self.conn = sql.connect(db)
        self.handle = self.conn.cursor()
        self.handle.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name text, age int, marital_status text, contact text)")
        self.conn.commit()

    def fetch(self):
        self.handle.execute("SELECT * FROM users")
        rows = self.handle.fetchall()
        return rows

    def insert(self, name, age, marital_status, contact):
        self.handle.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (name, age, marital_status, contact))
        self.conn.commit()

    def remove(self, id):
        self.handle.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, age, marital_status, contact):
        self.handle.execute("UPDATE users SET name = ?, age = ?, marital_status = ?, contact = ? WHERE id = ?",
                            (name, age, marital_status, contact, id))
        self.conn.commit()

    def __del__(self):  # this is a destructor
        self.conn.close()


db = Database('users.db')
db.insert("Alvin Mukiibi", 23, "Engaged", "777")
