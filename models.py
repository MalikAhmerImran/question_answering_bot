from pydantic import BaseModel,EmailStr



class User(BaseModel):
    email:str
    password:str
    is_verified:bool=False

class Email(BaseModel):
    email:EmailStr

    