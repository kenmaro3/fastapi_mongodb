from typing import List

from fastapi.responses import JSONResponse, Response
from fastapi import Body, status, HTTPException
from fastapi.encoders import jsonable_encoder

from api.schemas import user as user_schema
import api.cruds.user as user_cruds
from api.db import db

from api.routers.base import router


@router.post("/", response_description="Add new user", response_model=user_schema.UserCreateResponse)
async def create_user(user_create: user_schema.UserCreateRequest = Body(...)):
    created_user = await user_cruds.create_user(db, user_create)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


@router.get(
    "/", response_description="List all users", response_model=List[user_schema.User]
)
async def list_users():
    return await user_cruds.get_users(db)


@router.get(
    "/{id}", response_description="Get a single user", response_model=user_schema.User
)
async def show_user(id: str):
    user = user_cruds.get_user(db, id)
    if user is not None:
        return user

    raise HTTPException(status_code=404, detail=f"user {id} not found")


@router.put("/{id}", response_description="Update a user", response_model=user_schema.User)
async def update_user(id: str, user_update: user_schema.UserUpdateRequest = Body(...)):
    user = {k: v for k, v in user_update.dict().items() if v is not None}

    if len(user) >= 1:
        update_result = await db["users"].update_one({"_id": id}, {"$set": user})

        if update_result.modified_count == 1:
            if (
                updated_user := await db["users"].find_one({"_id": id})
            ) is not None:
                return updated_user

    if (existing_user := await db["users"].find_one({"_id": id})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"user {id} not found")

@router.put("/{id}/files", response_description="Add a file to user", response_model=user_schema.User)
async def update_user(id: str, user_add_file: user_schema.UserAddFileRequest = Body(...)):
    target_user = await db["users"].find_one({"_id": id})
    if target_user is None:
        raise HTTPException(status_code=404, detail=f"user {id} not found")
    print("\n\nhere")
    print(target_user)
    file_to_be_added = jsonable_encoder(user_add_file)
    if target_user.get("files") is None:
        print("file is None")
        target_user["files"] = [file_to_be_added]
        update_result = await db["users"].update_one({"_id": id}, {"$set": target_user})
        changed_user = await db["users"].find_one({"_id": id})
        return changed_user
    else:
        assert(isinstance(target_user.get("files"), list))
        target_user.get("files").append(file_to_be_added)
        update_result = await db["users"].update_one({"_id": id}, {"$set": target_user})
        changed_user = await db["users"].find_one({"_id": id})
        return changed_user

@router.put("/{id}/files/{file_id}/results", response_description="Add a result to file", response_model=user_schema.User)
async def update_user(id: str, file_id: str, user_add_result: user_schema.UserAddResultRequest = Body(...)):
    target_user = await db["users"].find_one({"_id": id})
    if target_user is None:
        raise HTTPException(status_code=404, detail=f"user {id} not found")
    print("\n\nhere")
    print(target_user)
    result_to_be_added = jsonable_encoder(user_add_result)

    target_file = None
    if target_user.get("files") is None:
        raise HTTPException(status_code=404, detail=f"no file found for user {id}")
        print("file is None")
        target_user["files"] = [file_to_be_added]
        update_result = await db["users"].update_one({"_id": id}, {"$set": target_user})
        changed_user = await db["users"].find_one({"_id": id})
        return changed_user
    else:


        for i, file in enumerate(target_user.get("files")):
            if file.get("_id") == file_id:
                target_file = file
                break
        if target_file is None:
            raise HTTPException(status_code=404, detail=f"no such a file found for user {id}")
        else:
            if target_file.get("results") is None:
                #target_file["results"] = [result_to_be_added]
                #target_user["files"]["results"] = [result_to_be_added]
                target_user["files"][i]["results"] = [result_to_be_added]
            else:
                assert(isinstance(target_user["files"]["results"], list))
                target_user["files"][i]["results"].append(result_to_be_added)
        
        update_result = await db["users"].update_one({"_id": id}, {"$set": target_user})
        changed_user = await db["users"].find_one({"_id": id})
        return changed_user
        

@router.delete("/{id}", response_description="Delete a user")
async def delete_user(id: str):
    delete_result = await user_cruds.delete_user(db, id)

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"user {id} not found")