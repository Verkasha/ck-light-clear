import sqlite3

from database.migration import create_book_table


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('database/database.sqlite',check_same_thread=False)

    def cursor(self) -> sqlite3.Cursor:
        return self.conn.cursor()

    @property
    def connection(self):
        return self.conn

    def migrate(self):
        create_book_table.handler(self.cursor())


db = DB()