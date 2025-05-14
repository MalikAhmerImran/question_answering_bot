from pydantic import BaseModel



class User(BaseModel):
    email:str
    password:str
    is_verified:bool=False

    