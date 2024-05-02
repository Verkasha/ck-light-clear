from fastapi import APIRouter, status

from app.exceptions import APIException
from database import db
from app.shemas import book

router = APIRouter(prefix="/book")


@router.get('/')
def get_books() -> list[book.Book]:
    cur = db.cursor()
    # TODO: Напишите запрос к базе данных, который вернет все книги
    # cur.execute('ВАШ SQL ЗАПРОС')
    # books = cur.fetchall()
    # return [book.Book(id=row[0], title=row[2], author=row[1], country=row[3], isbn=row[5], year=int(row[4])) for row in books]
    return []


@router.get('/{book_id}')
def get_book(book_id: int):
    cur = db.cursor()
    # TODO: Напишите запрос к базе данных, который вернет книгу с указанным id
    # cur.execute('ВАШ SQL ЗАПРОС', (book_id,))
    # row = cur.fetchone()
    # if row is None:
    #     raise APIException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    # return book.Book(id=row[0], title=row[1], author=row[2], country=row[3], isbn=row[4], year=int(row[5]))
    return None


@router.delete('/{book_id}')
def delete_book(book_id: int):
    cur = db.cursor()
    # TODO: Напишите запрос к базе данных, который удалит книгу с указанным id
    # cur.execute('ВАШ SQL ЗАПРОС', (book_id,))
    # db.connection.commit()
    # if cur.rowcount == 0:
    #     raise APIException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"message": "Book deleted"}


@router.post('/')
def add_book(request: book.BookCreate):
    cur = db.cursor()
    # TODO: Напишите запрос к базе данных, который добавит новую книгу
    # cur.execute('ВАШ SQL ЗАПРОС', (request.author, request.country, request.title, request.year, request.isbn))
    # db.connection.commit()
    return {"message": "Book added"}


@router.put('/{book_id}')
def update_book(book_id: int, request: book.BookUpdate):
    cur = db.cursor()
    # TODO: Напишите запрос к базе данных, который обновит информацию о книге с указанным id
    # cur.execute('ВАШ SQL ЗАПРОС', (request.author, request.country, request.title, request.year, request.isbn, book_id))
    # db.connection.commit()
    # if cur.rowcount == 0:
    #     raise APIException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"message": "Book updated"}