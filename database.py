import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


def get_collection(collection_name:str):
    return (
        MongoClient(os.getenv("local_db_url"))
        [os.getenv("data_base")]
        [collection_name]
    )



