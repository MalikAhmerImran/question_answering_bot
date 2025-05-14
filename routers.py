from models import User
from fastapi.routing import APIRouter
from database import add_user
user_router=APIRouter(prefix="/user")


@user_router.post("/register")
async def user_registration(request:User):
    return add_user(data=request)


