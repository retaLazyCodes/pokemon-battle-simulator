import requests
from bs4 import BeautifulSoup
from typing import Dict, List


class Pokedex:
    """A class for interacting with Pokémon data through the PokeAPI."""

    BASE_URL = "https://pokeapi.co/api/v2/"

    @staticmethod
    def get_pokemon_info(name: str) -> Dict:
        """
        Retrieves information about a Pokémon, including its stats, types, and evolutionary chain.

        :param name: The name of the Pokémon to retrieve information for. The name will be converted to lowercase
                    for the API request and capitalized in the returned dictionary.
        :return: A dictionary containing the Pokémon's name, HP, attack, defense, types, and evolution chain.
        """
        response = requests.get(f"{Pokedex.BASE_URL}pokemon/{name.lower()}")
        if response.status_code == 200:
            data = response.json()
            stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
            types = [
                type_info["type"]["name"].capitalize() for type_info in data["types"]
            ]
            evolution_chain = Pokedex.get_evolution_chain(name.lower())
            return {
                "name": name.capitalize(),
                "hp": stats["hp"],
                "attack": stats["attack"],
                "defense": stats["defense"],
                "speed": stats["speed"],
                "types": types,
                "evolution_chain": evolution_chain,
            }
        else:
            raise ValueError(f"Error al obtener información de {name}")

    @staticmethod
    def get_evolution_chain(name: str) -> List[tuple]:
        """
        Returns a list of Pokémon in the evolutionary chain for the given Pokémon.

        :param name: The name of the Pokémon whose evolution chain is to be retrieved.
        :return: A list of tuples with Pokémon name and a boolean indicating if it evolves by level.
        """
        url = f"https://pokemondb.net/pokedex/{name}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Error fetching page: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")

        evo_chain = []

        evo_div = soup.find("div", class_="infocard-list-evo")
        if not evo_div:
            return evo_chain

        infocards = evo_div.find_all("div", class_="infocard")
        arrows = evo_div.find_all("span", class_="infocard-arrow")

        for index, infocard in enumerate(infocards):
            name_tag = infocard.find("a", class_="ent-name")
            pokemon_name = name_tag.text.lower()

            evolves_by_level = False
            if index < len(arrows):
                level_info = arrows[index].find("small")
                if level_info and "level" in level_info.text.lower():
                    evolves_by_level = True

            evo_chain.append((pokemon_name, evolves_by_level))

        return evo_chain
