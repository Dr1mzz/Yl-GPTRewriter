import sqlite3
import os
import hashlib

script_dir = os.path.dirname(__file__)
rel_path = "resources/GPTRewriter.db"
abs_db_path = os.path.join(script_dir, rel_path)


class UserDao:
    def __init__(self):
        self.con = sqlite3.connect(abs_db_path)
        self.cur = self.con.cursor()

    def save(self, name, login, password):
        result = hashlib.md5(password.encode()).hexdigest()
        query = 'INSERT INTO user(name, login, password) VALUES (?, ?, ?)'
        self.cur.execute(query, (name, login, result))
        self.con.commit()

    def get(self, login):
        query = 'SELECT * FROM user WHERE login = ?'
        user = self.cur.execute(query, (login,)).fetchone()
        return user