from fastapi.encoders import jsonable_encoder

from api.schemas import user as user_schema
import api.cruds.user as user_crud
from api.db import db

async def create_user(db, user_create: user_schema.UserCreateRequest):
    user = jsonable_encoder(user_create)
    new_user = await db["users"].insert_one(user)
    created_user = await db["users"].find_one({"_id": new_user.inserted_id})
    return created_user


async def get_users(db):
    return await db["users"].find().to_list(1000)

async def get_user(db, id: int):
    return await db["users"].find_one({"_id": id})

async def delete_user(db, id: int):
    return await db["users"].delete_one({"_id": id})
