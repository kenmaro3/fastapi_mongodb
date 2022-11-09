from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId

import api.schemas.id as id_model

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


class FileCreateRequest(FileBase):
    pass

class FileCreateResponse(FileBase):
    pass


class FileUpdateRequest(FileBase):
    pass

class FileUpdateResponse(FileBase):
    pass


class File(FileBase):
    pass