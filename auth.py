import jwt
from fastapi.exceptions import HTTPException
from database import get_collection
from dotenv import dotenv_values

config_credentials=dotenv_values(".env")



def create_token(token):
    token={
        "username":token.get("email")
    }
    return jwt.encode(token,config_credentials["SECRET"],algorithm="HS256") 


def verify_token(token:str):
    try:
        payload=jwt.decode(token,config_credentials["SECRET"], algorithms="HS256")
        user=get_collection(collection_name="users").find_one({"email":payload.get("username")})
    except Exception as e:
        print("JWT Decode Error:", e)
        raise HTTPException(status_code=404,detail="User does not exits or invalid token")
    return user
