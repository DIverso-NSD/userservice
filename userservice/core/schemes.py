from pydantic import BaseModel
from pydantic.fields import Field


class User(BaseModel):
    login: str = Field(
        ...,
        example="kuder",
    )
    telegram: str = Field(..., example="kuderr")


class File(BaseModel):
    name: str = Field(..., example="NSD.zip")
