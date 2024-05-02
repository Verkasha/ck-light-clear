from fastapi import FastAPI
from starlette.responses import FileResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.exceptions import APIException
from app.routes import router
import uvicorn

from fastapi.exception_handlers import http_exception_handler

from database import db

app = FastAPI(title='CK Light', threaded=False)  # Создание экземпляра приложения FastAPI

origins = [
    "http://127.0.0.1:7000",
    "http://localhost:7000",
    "http://127.0.0.1:7500",
    "http://localhost:7500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрация маршрутов
app.include_router(router)

# Делаем доступ к статичным файлам.
app.mount("/", StaticFiles(directory="resource/dist"), name="static")


# Делаем все перенаправления которые не зарегистрированы на Vue
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    if isinstance(exc, APIException):
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
    if exc.status_code == 404:
        return FileResponse('resource/dist/index.html', media_type="text/html")
    return await http_exception_handler(request, exc)


if __name__ == "__main__":
    db.migrate()
    uvicorn.run(app, host="127.0.0.1", port=7500, reload=False)

