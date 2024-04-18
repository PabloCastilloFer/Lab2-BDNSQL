import requests
from pymongo import MongoClient

# Conexión a la base de datos de MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['pokemones']
collection = db['pokemon']

# Obtener información de la API de Pokémon
response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=50')
data = response.json()

# Iterar sobre cada Pokémon en la respuesta
for pokemon_data in data['results']:
    # Obtener información detallada del Pokémon
    pokemon_response = requests.get(pokemon_data['url'])
    pokemon_data = pokemon_response.json()

    # Extraer el nombre, tipo, peso y altura del Pokémon
    name = pokemon_data['name']
    types = [t['type']['name'] for t in pokemon_data['types']]
    weight = pokemon_data['weight']
    height = pokemon_data['height']

    # Guardar la información en la base de datos
    pokemon = {'name': name, 'types': types, 'weight': weight, 'height': height}
    collection.insert_one(pokemon)

print('Información de los Pokémon guardada en la base de datos.')
