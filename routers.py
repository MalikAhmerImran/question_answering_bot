from models import User
from fastapi import Request
from fastapi.routing import APIRouter
from database import add_user
from utils import verify_token,send_email
from database import get_collection
user_router=APIRouter(prefix="/user")


@user_router.post("/register")
async def user_registration(request:User):
    await send_email(email=request.email,instance=User)
    return add_user(data=request)



@user_router.get("/verification")
async def email_verifcation(token:str):
    user=verify_token(token=token)
    if user and user["is_verified"] is False:
       get_collection(collection_name="users").update_one(
        {"_id": user["_id"]},
        {"$set": {"is_verified": True}}
    )
    return  {
            "message":"verified"
        }
    