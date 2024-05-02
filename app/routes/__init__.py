__all__ = ['router']

from fastapi import APIRouter
from .book import router as book_router

router = APIRouter(prefix='/api/v1')

router.include_router(book_router)