from pydantic import BaseModel


class Addition(BaseModel):
    additional_info: str
    additional_number: int


class Entity(BaseModel):
    title: str
    verified: bool
    addition: Addition
    important_numbers: list[int]
