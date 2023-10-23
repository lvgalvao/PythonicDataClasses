from pydantic import BaseModel, HttpUrl


class Personagem(BaseModel):
    """
    Representa um personagem com atributos específicos.

    Args:
        id (int): O identificador único do personagem.
        name (str): O nome do personagem.
        status (str): O status atual do personagem.
        species (str): A espécie do personagem.
        gender (str): O gênero do personagem.
        url (HttpUrl): O URL associado ao personagem, deve ser uma string válida de URL.

    Example:
        Instanciando e acessando os atributos de `Personagem`:

        ```python
        rick = Personagem(
            id=1,
            name="Rick Sanchez",
            status="Alive",
            species="Human",
            gender="Male",
            url="https://rickandmortyapi.com/api/location/3"
        )
        print(rick.id)  # Output: 1

        morty = Personagem(
            id=2,
            name="Morty Smith",
            status="Alive",
            species="Human",
            gender="Male",
            url="https://rickandmortyapi.com/api/location/3"
        )
        print(morty.name)  # Output: 'Morty Smith'
        ```

    Você pode acessar os atributos como `rick.id`, `rick.name`, etc.
    """

    id: int
    name: str
    status: str
    species: str
    gender: str
    url: HttpUrl  # O campo URL deve ser uma string.
