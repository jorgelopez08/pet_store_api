"""Pydantic models"""

from pydantic import BaseModel
from pydantic import Field

class Pet(BaseModel):
    id: int = Field(default=None)
    name: str = Field(...)

    class Config:
        schema_extra = {
            "example":{
                "name":"Dash"
            }
        }