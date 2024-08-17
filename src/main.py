import json

from core.pokedex import Pokedex


def main():
    with open('batallas.json') as f:
        data = json.load(f)


    for battle_data in data['batallas']:
        pokemon1_name = battle_data['Pokemon 1']
        pokemon2_name = battle_data['Pokemon 2']
        points = battle_data['Puntos']

        print(f"\nObteniendo datos de {pokemon1_name}")
        pokemon1 = Pokedex.get_pokemon_info(pokemon1_name)
        print(f"Obteniendo datos de {pokemon2_name}")
        pokemon2 = Pokedex.get_pokemon_info(pokemon2_name)
        print(f"{pokemon1}\n{pokemon2}")

if __name__ == "__main__":
    main()
