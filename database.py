import os
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def get_collection(collection_name:str):
    return (
        MongoClient(os.getenv("local_db_url"))
        [os.getenv("data_base")]
        [collection_name]
    )


def add_user(data):
    collection=get_collection(collection_name="users")
    if collection.find_one({"email":data.email}):
        raise HTTPException(status_code=409,detail="User already exits.")

    user_data=collection.insert_one(data.dict())
    return {
        "message":"User register successfully."
    }



