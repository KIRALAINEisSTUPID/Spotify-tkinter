import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('users_list.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists users(
                id integer primary key,
                email varchar,
                password varchar)""")

    def add_user(self, email,password):
        self.cursor.execute("""insert into users
                            (email, password)
                            values (?, ?)""",
                            (email,password))
        self.connection.commit()
#
    def show_users(self):
        users = self.cursor.execute("select * from users")
        return users.fetchall()

    def get_user(self, email, password):
        user = self.cursor.execute("select * from users where email=? and password=?",
                                   (email, password))
        return user.fetchone()



db = Database()
