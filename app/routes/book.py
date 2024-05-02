from fastapi import APIRouter, status

from app.exceptions import APIException
from database import db
from app.shemas import book

router = APIRouter(prefix="/book")


@router.get('/')
def get_books() -> list[book.Book]:
    cur = db.cursor()
    cur.execute('SELECT id, author, country, title, year, isbn FROM books')

    rows = cur.fetchall()
    books = [book.Book(id=row[0], author=row[1], country=row[2], title=row[3], year=int(row[4]), isbn=row[5]) for row in rows]
    return books


@router.get('/{book_id}')
def get_book(book_id: int):
    cur = db.cursor()
    cur.execute('SELECT id, author, country, title, year, isbn FROM books WHERE id = ?', (book_id,))
    row = cur.fetchone()
    if row is None:
        raise APIException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book.Book(id=row[0], title=row[2], author=row[1], country=row[3], isbn=row[5], year=int(row[4]))


@router.delete('/{book_id}')
def delete_book(book_id: int):
    cur = db.cursor()
    cur.execute('DELETE FROM books WHERE id = ?', (book_id,))
    db.connection.commit()
    if cur.rowcount == 0:
        raise APIException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"message": "Book deleted"}


@router.post('/')
def add_book(request: book.BookCreate):
    cur = db.cursor()
    cur.execute('INSERT INTO books (author, country, title, year, isbn) VALUES (?, ?, ?, ?, ?)',
                (request.author, request.country, request.title, request.year, request.isbn))
    db.connection.commit()
    return {"message": "Book added"}


@router.put('/{book_id}')
def update_book(book_id: int, request: book.BookUpdate):
    cur = db.cursor()
    cur.execute('UPDATE books SET author = ?, country = ?, title = ?, year = ?, isbn = ? WHERE id = ?',
                (request.author, request.country, request.title, request.year, request.isbn, book_id))
    db.connection.commit()
    if cur.rowcount == 0:
        raise APIException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"message": "Book updated"}
