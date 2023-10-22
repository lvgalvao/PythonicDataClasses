import requests
import csv

def fetch_characters() -> list:
    url = f'https://rickandmortyapi.com/api/character/?page=1'
    response = requests.get(url)
    data = response.json()
    characters = []

    for item in data['results']:
        character = {
            'id': item['id'],
            'name': item['name'],
            'status': item['status'],
            'species': item['species'],
            'gender': item['gender'],
            'url': item['location']['url']
        }
        characters.append(character)

    return characters

def save_to_csv(characters, file_name='characters.csv'):
    # Especificando os nomes das colunas para o CSV.
    field_names = ['id', 'name', 'status', 'species', 'gender', 'url']
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        
        writer.writeheader()
        for character in characters:
            writer.writerow(character)  # 'character' já é um dicionário, então podemos passá-lo diretamente.

if __name__ == "__main__":
    lista_de_characters = fetch_characters()
    save_to_csv(lista_de_characters)