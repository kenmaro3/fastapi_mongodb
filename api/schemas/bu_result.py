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
                "coordinates": "result_word",
                "word": "result_word",

            }
        }


class ResultCreateRequest(ResultBase):
    pass

class ResultCreateResponse(ResultBase):
    pass


class ResultUpdateRequest(ResultBase):
    pass

class ResultUpdateResponse(ResultBase):
    pass

class ResultAddFileRequest(FileBase):
    pass

class ResultAddFileResponse(ResultBase):
    pass


class Result(ResultBase):
    #name: str
    
    pass