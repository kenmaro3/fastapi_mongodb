from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

import api.schemas.id as id_model

class ResultBase(BaseModel):
    id: id_model.PyObjectId = Field(default_factory=id_model.PyObjectId, alias="_id")
    word: str
    coordinates: List[int]
    width: int
    height: int
    type: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "word": "result_word",
                "coordinates": [100, 200],
                "width": 100,
                "height": 40,
                "type": "type",

            }
        }

class FileBase(BaseModel):
    id: id_model.PyObjectId = Field(default_factory=id_model.PyObjectId, alias="_id")
    path: str
    updated_ts: str
    results: Optional[dict]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "path": "1.png",
                "updated_ts": "2022-11-09",
            }
        }

class UserBase(BaseModel):
    id: id_model.PyObjectId = Field(default_factory=id_model.PyObjectId, alias="_id")
    name: str
    password: str
    files: Optional[List[dict]]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "user",
                "password": "1234",
            }
        }


class UserCreateRequest(UserBase):
    pass

class UserCreateResponse(UserBase):
    pass


class UserUpdateRequest(UserBase):
    pass

class UserUpdateResponse(UserBase):
    pass

class UserAddFileRequest(FileBase):
    pass

class UserAddFileResponse(UserBase):
    pass

class UserAddResultRequest(ResultBase):
    pass

class UserAddFileResponse(UserBase):
    pass


class User(UserBase):
    #name: str
    
    pass