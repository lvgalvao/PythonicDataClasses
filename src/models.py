from dataclasses import dataclass
import re

@dataclass
class Personagem:
    id: int
    name: str
    status: str
    species: str
    gender: str
    url: str  # O campo URL deve ser uma string.