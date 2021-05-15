from pydantic import BaseModel
from pydantic.fields import Field


class User(BaseModel):
    login: str = Field(
        ...,
        example="penis",
    )
    telegram: str = Field(
        ...,
        example="penis"
    )


class File(BaseModel):
    name: str = Field(
        ...,
        example="penis.zip"
    )
