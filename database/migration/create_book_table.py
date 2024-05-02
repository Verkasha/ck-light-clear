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

    # TODO: Напишите запрос к базе данных, который создаст таблицу books, если она еще не существует
    # Проверка, что таблица не существует
    # if cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'").fetchone():
    #     return

    # cur.execute("""
    #     ВАШ SQL ЗАПРОС ДЛЯ СОЗДАНИЯ ТАБЛИЦЫ
    # """)
    pass

