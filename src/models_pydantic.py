from pydantic import BaseModel, HttpUrl

class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    gender: str
    url: HttpUrl 