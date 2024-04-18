from pymongo import MongoClient
import json

# Conexión a la base de datos
client = MongoClient('localhost', 27017)
db = client['pokemones']  # Nombre de la base de datos
collection = db['pokemon']  # Nombre de la colección

# Obtener pesos y alturas de los Pokémon
weights = []
heights = []
for pokemon in collection.find({}, {'_id': 0, 'weight': 1, 'height': 1}):
    weights.append(pokemon['weight'])
    heights.append(pokemon['height'])

# Calcular promedio de pesos y alturas
average_weight = sum(weights) / len(weights)
average_height = sum(heights) / len(heights)

# Guardar los resultados en un archivo JSON
data = {
    'average_weight': average_weight,
    'average_height': average_height
}
with open('average_stats.json', 'w') as file:
    json.dump(data, file)

print("Promedios de peso y altura calculados y guardados en average_stats.json")
