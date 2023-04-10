from typing import Any
from starlette.exceptions import HTTPException as StarletteHTTPException

class customException(StarletteHTTPException):
    def __init__(self,status_code: int,message:str):
        self.status_code = status_code
        self.message     = message

class NotFound(StarletteHTTPException):
    def __init__(self,status_code: int):
        self.status_code = status_code

class Redirect(StarletteHTTPException):
    def __init__(self,status_code: int,url:str):
        self.status_code = status_code
        self.url         = url


class Unauthorised(StarletteHTTPException):
    def __init__(self):
        self.status_code = 401
        self.message         = 'Unauthorized'