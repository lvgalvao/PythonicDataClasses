import requests
from models_dataclass import Character  # Certifique-se de importar o modelo correto
import csv
# from pydantic import ValidationError  # Importado para tratamento de erro

def fetch_characters() -> list:
    url = f'https://rickandmortyapi.com/api/character/?page=1'
    response = requests.get(url)
    data = response.json()
    characters = []

    for index, item in enumerate(data['results'], start=1):
        try:
            # Aqui, Pydantic irá validar os dados automaticamente ao criar o modelo
            character = Character(
                id=item['id'],
                name=item['name'],
                status=item['status'],
                species=item['species'],
                gender=item['gender'],
                url=item['location']['url']
            )
            characters.append(character)

        except ValueError as e:
            print(f"Error in {index}: {e}")
            continue

    return characters

def save_to_csv(characters, file_name='characters.csv'):
    # Especificando os nomes das colunas para o CSV.
    field_names = ['id', 'name', 'status', 'species', 'gender', 'url']
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        writer.writeheader()
        for character in characters:
            # Convertendo o objeto dataclass em um dicionário antes de escrever.
            writer.writerow(character.__dict__)

if __name__ == "__main__":

    lista_de_characters = fetch_characters()
    save_to_csv(lista_de_characters)
