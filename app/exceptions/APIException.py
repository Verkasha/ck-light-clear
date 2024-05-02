from fastapi import HTTPException


class APIException(HTTPException):
    def __init__(self, status_code, detail=None, headers=None):
        super().__init__(status_code=status_code, detail=detail, headers=headers)
