from pymongo import MongoClient
import json

# Conexión a la base de datos
client = MongoClient('localhost', 27017)
db = client['pokemones']  # Nombre de la base de datos
collection = db['pokemon']  # Nombre de la colección

# Obtener tipos de Pokémon y contar cuántos hay de cada tipo
types_count = {}
for pokemon in collection.find({}, {'_id': 0, 'types': 1}):
    for pokemon_type in pokemon['types']:
        types_count[pokemon_type] = types_count.get(pokemon_type, 0) + 1

# Guardar los resultados en un archivo JSON
with open('types_count.json', 'w') as file:
    json.dump(types_count, file)

print("Datos extraídos y guardados en types_count.json")
