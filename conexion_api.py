pip install -U nekosbest

import requests
import pandas as pd
import json

"""
##url = "https://cat-fact.herokuapp.com/facts"
url = "https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php?pokedex=all"
headers = {"Accept-Encoding": "gzip, deflate"}

response = requests.get(url, headers=headers)

print(response.text)

data = json.loads(response.text)
data
df = pd.DataFrame(data)
df.head()
"""


resp = requests.get("https://courses.cs.washington.edu/courses/cse154/webservices/pokedex/pokedex.php?pokemon=pikachu")
data = resp.json()
print(data["results"][0]["url"])

url = "https://cat-fact.herokuapp.com/facts"
headers = {"Accept-Encoding": "gzip, deflate"}
response = requests.get(url, headers=headers)
data = response.json()




import requests
import pandas as pd

# Función para obtener información sobre un Pokémon específico
def obtener_informacion_pokemon(numero):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}pokemon/{numero}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error al obtener información del Pokémon {numero}. Código de estado: {response.status_code}")
        return None

# Función para obtener información sobre los tipos de movimientos que un Pokémon puede usar
def obtener_tipos_movimientos_pokemon(numero):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}pokemon/{numero}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        tipos_movimientos = set()
        for movimiento in data["moves"]:
            movimiento_url = movimiento["move"]["url"]
            movimiento_response = requests.get(movimiento_url)
            if movimiento_response.status_code == 200:
                movimiento_data = movimiento_response.json()
                for tipo in movimiento_data["type"]["name"]:
                    tipos_movimientos.add(tipo)
        return list(tipos_movimientos)
    else:
        print(f"Error al obtener información del Pokémon {numero}. Código de estado: {response.status_code}")
        return None

# Función para obtener información sobre los stats de un Pokémon
def obtener_stats_pokemon(numero):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}pokemon/{numero}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        return stats
    else:
        print(f"Error al obtener información del Pokémon {numero}. Código de estado: {response.status_code}")
        return None

# Función para obtener información sobre las habilidades de un Pokémon
def obtener_habilidades_pokemon(numero):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}pokemon/{numero}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        habilidades = [habilidad["ability"]["name"] for habilidad in data["abilities"]]
        return habilidades
    else:
        print(f"Error al obtener información del Pokémon {numero}. Código de estado: {response.status_code}")
        return None

# Ejemplo de uso
pokemon_numero = 1  # Bulbasaur
info_pokemon = obtener_informacion_pokemon(pokemon_numero)

if info_pokemon:
    print(f"Nombre: {info_pokemon['name']}")
    print(f"Altura: {info_pokemon['height']} decímetros")
    print(f"Peso: {info_pokemon['weight']} hectogramos")
    print(f"Tipos: {[tipo['type']['name'] for tipo in info_pokemon['types']]}")
    print(f"Experiencia base: {info_pokemon['base_experience']}")
    
    stats = obtener_stats_pokemon(pokemon_numero)
    if stats:
        print(f"\nStats de {info_pokemon['name']}:")
        for stat, valor in stats.items():
            print(f"{stat.capitalize()}: {valor}")
            
    habilidades = obtener_habilidades_pokemon(pokemon_numero)
    if habilidades:
        print(f"\nHabilidades de {info_pokemon['name']}:")
        for habilidad in habilidades:
            print(habilidad)
else:
    print("No se pudo obtener información del Pokémon.")

# Crear un DataFrame con la información del Pokémon
data = {
    "Nombre": [info_pokemon['name']],
    "Altura": [info_pokemon['height']],
    "Peso": [info_pokemon['weight']],
    "Tipos": [[tipo['type']['name'] for tipo in info_pokemon['types']]],
    "Experiencia Base": [info_pokemon['base_experience']],
    "HP": [stats['hp']],
    "Ataque": [stats['attack']],
    "Defensa": [stats['defense']],
    "Ataque Especial": [stats['special-attack']],
    "Defensa Especial": [stats['special-defense']],
    "Velocidad": [stats['speed']],
    "Habilidades": [habilidades]
}

df = pd.DataFrame(data)

print("\nDataFrame creado a partir de la información del Pokémon:")
print(df)