import json
import os

from core import Pokedex
from battle import Battle


def main():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, "data", "batallas.json")

    with open(file_path) as f:
        data = json.load(f)

    for battle_data in data["batallas"]:
        pokemon1_name = battle_data["Pokemon 1"]
        pokemon2_name = battle_data["Pokemon 2"]
        points = battle_data["Puntos"]

        print(f"\nGetting data from {pokemon1_name}")
        pokemon1 = Pokedex.get_pokemon_info(pokemon1_name)
        print(f"Getting data from {pokemon2_name}")
        pokemon2 = Pokedex.get_pokemon_info(pokemon2_name)
        print(f"{pokemon1}\n{pokemon2}")

        battle = Battle(pokemon1, pokemon2)
        battle.start_battle(points)


if __name__ == "__main__":
    main()
