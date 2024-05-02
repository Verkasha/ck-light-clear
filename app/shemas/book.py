from pydantic import BaseModel, Field


class BookBase(BaseModel):
    title: str = Field(..., description="Название книги", min_length=1, max_length=200)
    author: str = Field(..., description="Имя автора книги", min_length=2, max_length=100)
    country: str = Field(..., description="Страна проживания автора", min_length=2, max_length=100)
    isbn: str = Field(..., description="ISBN книги", min_length=10, max_length=13)
    year: int = Field(..., description="Год издания книги", gt=0, examples=[1920])


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
