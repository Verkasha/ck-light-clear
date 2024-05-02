import sqlite3


def handler(cur: sqlite3.Cursor):
    # Создание таблицы
    # Таблица книги
    # id - идентификатор
    # author - ФИО
    # country - страна проживания автора
    # title - название книги
    # year - год издания
    # isbn - ISBN книги

    # Проверка, что таблица не существует
    if cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'").fetchone():
        return

    cur.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            country TEXT NOT NULL,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            isbn TEXT NOT NULL
        )
    """)

