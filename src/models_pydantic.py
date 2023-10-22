from pydantic import BaseModel, HttpUrl

class Personagem(BaseModel):
    id: int
    name: str
    status: str
    species: str
    gender: str
    url: HttpUrl 