from pydantic import BaseModel as PydanticModel, Field,EmailStr,ValidationError
from exception import customException
from controller.http import http_codes

class BaseModel(PydanticModel):
    def __init__(self, **data):
        try:
            super().__init__(**data)
        except ValidationError as e:
            err = e.errors()
            if err[0]['loc'][0]: # name of the Field that failed in validation
                raise customException(message=f"invalid {err[0]['loc'][0]}", status_code=400)
            raise customException(message=http_codes[400], status_code=400)
        
class Example(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
        