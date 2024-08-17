import requests

class Pokedex:
    """A class for interacting with Pokémon data through the PokeAPI."""

    BASE_URL = "https://pokeapi.co/api/v2/"

    @staticmethod
    def get_pokemon_info(name: str) -> dict:
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
            types = [type_info["type"]["name"].capitalize() for type_info in data["types"]]
            evolution_chain = Pokedex.get_evolution_chain(name.lower())
            return {
                "name": name.capitalize(),
                "hp": stats["hp"],
                "attack": stats["attack"],
                "defense": stats["defense"],
                "speed": stats["speed"],
                "types": types,
                "evolution_chain": evolution_chain
            }
        else:
            raise ValueError(f"Error al obtener información de {name}")

    @staticmethod
    def get_evolution_chain(name: str) -> list[str]:
        """
        Returns a list of Pokémon names in the evolutionary chain for the given Pokémon.

        :param name: The name of the Pokémon whose evolution chain is to be retrieved.
        :return: A list of Pokémon names in the evolutionary chain.

        TODO: Implement the logic to fetch the evolution chain from the PokeAPI.
        """
        return []
