from pydantic import BaseModel


class Character(BaseModel):
    name: str
    last_name: str
    age: int
    