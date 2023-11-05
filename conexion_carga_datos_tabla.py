
import psycopg2
import requests

# Conexión a la API de Pokémon
def obtener_datos_pokemon(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            'nombre': pokemon_data['name'],
            'altura': pokemon_data['height'],
            'peso': pokemon_data['weight'],
            'tipos': ','.join([tipo['type']['name'] for tipo in pokemon_data['types']]),
            'experiencia_base': pokemon_data['base_experience'],
            'hp': next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'hp'),
            'ataque': next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'attack'),
            'defensa': next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'defense'),
            'ataque_especial': next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'special-attack'),
            'defensa_especial': next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'special-defense'),
            'velocidad': next(stat['base_stat'] for stat in pokemon_data['stats'] if stat['stat']['name'] == 'speed')
        }
    else:
        print(f"Error al obtener datos del Pokémon {pokemon_id}. Código de estado: {response.status_code}")
        return None

# Conexión a la base de datos de Redshift
url = "data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws"
data_base = "data-engineer-database"
user = "marquezlucasa_coderhouse"
with open("E:\de\crs.txt", 'r') as f:
    pwd = f.read()

try:
    conn = psycopg2.connect(
        host='data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com',
        dbname=data_base,
        user=user,
        password=pwd,
        port='5439'
    )
    print("Connected to Redshift successfully!")

except Exception as e:
    print("Unable to connect to Redshift.")
    print(e)

# Cursor para ejecutar comandos SQL
cur = conn.cursor()

# Obtener y cargar los datos de los primeros 150 Pokémon en la base de datos de Redshift
for i in range(1, 151):
    pokemon_data = obtener_datos_pokemon(i)
    if pokemon_data:
        cur.execute("""
            INSERT INTO pokemon (
                nombre, altura, peso, tipos, experiencia_base, hp, ataque, defensa, ataque_especial, defensa_especial, velocidad
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            pokemon_data['nombre'],
            pokemon_data['altura'],
            pokemon_data['peso'],
            pokemon_data['tipos'],
            pokemon_data['experiencia_base'],
            pokemon_data['hp'],
            pokemon_data['ataque'],
            pokemon_data['defensa'],
            pokemon_data['ataque_especial'],
            pokemon_data['defensa_especial'],
            pokemon_data['velocidad']
        ))
    else:
        print(f"No se pudieron obtener datos para el Pokémon {i}.")

# Confirmar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()