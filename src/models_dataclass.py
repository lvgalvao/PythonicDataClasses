from dataclasses import dataclass
import re

@dataclass
class Character:
    id: int
    name: str
    status: str
    species: str
    gender: str
    url: str  # O campo URL deve ser uma string.

    def __post_init__(self):
        # Regex simplificada para validar a maioria das URLs
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:[a-zA-Z0-9.-]|%[0-9a-fA-F]{2})+'  # domain
            r'(?:/[a-zA-Z0-9@:%._+~#?&/=]*)?'  # components of the path, query, fragment
            r'$', re.IGNORECASE)

        if not re.match(regex, self.url):
            raise ValueError(f"A URL fornecida não é válida: '{self.url}'")  # Adicione aspas para identificar espaços em branco ou strings vazias.