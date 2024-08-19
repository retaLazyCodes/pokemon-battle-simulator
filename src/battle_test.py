from battle import Battle
from core import Pokemon

pokemon_data = [
    {
        "name": "Dragonite",
        "hp": 91,
        "attack": 134,
        "defense": 95,
        "speed": 80,
        "types": ["Dragon", "Flying"],
        "evolution_chain": [
            ("dratini", True),
            ("dragonair", True),
            ("dragonite", False),
        ],
    },
    {
        "name": "Salamence",
        "hp": 95,
        "attack": 135,
        "defense": 80,
        "speed": 100,
        "types": ["Dragon", "Flying"],
        "evolution_chain": [("bagon", True), ("shelgon", True), ("salamence", False)],
    },
    {
        "name": "Infernape",
        "hp": 76,
        "attack": 104,
        "defense": 71,
        "speed": 108,
        "types": ["Fire", "Fighting"],
        "evolution_chain": [
            ("chimchar", True),
            ("monferno", True),
            ("infernape", False),
        ],
    },
    {
        "name": "Greninja",
        "hp": 72,
        "attack": 95,
        "defense": 67,
        "speed": 122,
        "types": ["Water", "Dark"],
        "evolution_chain": [
            ("froakie", True),
            ("frogadier", True),
            ("greninja", False),
        ],
    },
    {
        "name": "Ralts",
        "hp": 28,
        "attack": 25,
        "defense": 25,
        "speed": 40,
        "types": ["Psychic", "Fairy"],
        "evolution_chain": [
            ("ralts", True),
            ("kirlia", True),
            ("gardevoir", False),
            ("gallade", False),
        ],
    },
    {
        "name": "Beldum",
        "hp": 40,
        "attack": 55,
        "defense": 80,
        "speed": 30,
        "types": ["Steel", "Psychic"],
        "evolution_chain": [("beldum", True), ("metang", True), ("metagross", False)],
    },
    {
        "name": "Duskull",
        "hp": 20,
        "attack": 40,
        "defense": 90,
        "speed": 25,
        "types": ["Ghost"],
        "evolution_chain": [
            ("duskull", True),
            ("dusclops", False),
            ("dusknoir", False),
        ],
    },
    {
        "name": "Gastly",
        "hp": 30,
        "attack": 35,
        "defense": 30,
        "speed": 80,
        "types": ["Ghost", "Poison"],
        "evolution_chain": [("gastly", True), ("haunter", False), ("gengar", False)],
    },
    {
        "name": "Shedinja",
        "hp": 1,
        "attack": 90,
        "defense": 45,
        "speed": 40,
        "types": ["Bug", "Ghost"],
        "evolution_chain": [
            ("nincada", True),
            ("ninjask", True),
            ("ninjask", False),
            ("shedinja", False),
        ],
    },
    {
        "name": "Groudon",
        "hp": 100,
        "attack": 150,
        "defense": 140,
        "speed": 90,
        "types": ["Ground"],
        "evolution_chain": [],
    },
    {
        "name": "Chansey",
        "hp": 250,
        "attack": 5,
        "defense": 5,
        "speed": 50,
        "types": ["Normal"],
        "evolution_chain": [("happiny", False), ("chansey", False), ("blissey", False)],
    },
    {
        "name": "Machamp",
        "hp": 90,
        "attack": 130,
        "defense": 80,
        "speed": 55,
        "types": ["Fighting"],
        "evolution_chain": [("machop", True), ("machoke", False), ("machamp", False)],
    },
    {
        "name": "Budew",
        "hp": 40,
        "attack": 30,
        "defense": 35,
        "speed": 55,
        "types": ["Grass", "Poison"],
        "evolution_chain": [("budew", False), ("roselia", False), ("roserade", False)],
    },
    {
        "name": "Hoppip",
        "hp": 35,
        "attack": 35,
        "defense": 40,
        "speed": 50,
        "types": ["Grass", "Flying"],
        "evolution_chain": [("hoppip", True), ("skiploom", True), ("jumpluff", False)],
    },
    {
        "name": "Gengar",
        "hp": 60,
        "attack": 65,
        "defense": 60,
        "speed": 110,
        "types": ["Ghost", "Poison"],
        "evolution_chain": [("gastly", True), ("haunter", False), ("gengar", False)],
    },
    {
        "name": "Alakazam",
        "hp": 55,
        "attack": 50,
        "defense": 45,
        "speed": 120,
        "types": ["Psychic"],
        "evolution_chain": [("abra", True), ("kadabra", False), ("alakazam", False)],
    },
    {
        "name": "Tyranitar",
        "hp": 100,
        "attack": 134,
        "defense": 110,
        "speed": 61,
        "types": ["Rock", "Dark"],
        "evolution_chain": [
            ("larvitar", True),
            ("pupitar", True),
            ("tyranitar", False),
        ],
    },
    {
        "name": "Metagross",
        "hp": 80,
        "attack": 135,
        "defense": 130,
        "speed": 70,
        "types": ["Steel", "Psychic"],
        "evolution_chain": [("beldum", True), ("metang", True), ("metagross", False)],
    },
    {
        "name": "Charmander",
        "hp": 39,
        "attack": 52,
        "defense": 43,
        "speed": 65,
        "types": ["Fire"],
        "evolution_chain": [
            ("charmander", True),
            ("charmeleon", True),
            ("charizard", False),
        ],
    },
    {
        "name": "Squirtle",
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "speed": 43,
        "types": ["Water"],
        "evolution_chain": [
            ("squirtle", True),
            ("wartortle", True),
            ("blastoise", False),
        ],
    },
    {
        "name": "Magikarp",
        "hp": 20,
        "attack": 10,
        "defense": 55,
        "speed": 80,
        "types": ["Water"],
        "evolution_chain": [("magikarp", True), ("gyarados", False)],
    },
    {
        "name": "Gyarados",
        "hp": 95,
        "attack": 125,
        "defense": 79,
        "speed": 81,
        "types": ["Water", "Flying"],
        "evolution_chain": [("magikarp", True), ("gyarados", False)],
    },
    {
        "name": "Garchomp",
        "hp": 108,
        "attack": 130,
        "defense": 95,
        "speed": 102,
        "types": ["Dragon", "Ground"],
        "evolution_chain": [("gible", True), ("gabite", True), ("garchomp", False)],
    },
    {
        "name": "Weavile",
        "hp": 70,
        "attack": 120,
        "defense": 65,
        "speed": 125,
        "types": ["Dark", "Ice"],
        "evolution_chain": [("sneasel", False), ("weavile", False)],
    },
    {
        "name": "Pikachu",
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "speed": 90,
        "types": ["Electric"],
        "evolution_chain": [("pichu", False), ("pikachu", False), ("raichu", False)],
    },
    {
        "name": "Onix",
        "hp": 35,
        "attack": 45,
        "defense": 160,
        "speed": 70,
        "types": ["Rock", "Ground"],
        "evolution_chain": [("onix", False), ("steelix", False)],
    },
    {
        "name": "Shuckle",
        "hp": 20,
        "attack": 10,
        "defense": 230,
        "speed": 5,
        "types": ["Bug", "Rock"],
        "evolution_chain": [],
    },
    {
        "name": "Rayquaza",
        "hp": 105,
        "attack": 150,
        "defense": 90,
        "speed": 95,
        "types": ["Dragon", "Flying"],
        "evolution_chain": [],
    },
    {
        "name": "Trapinch",
        "hp": 45,
        "attack": 100,
        "defense": 45,
        "speed": 10,
        "types": ["Ground"],
        "evolution_chain": [("trapinch", True), ("vibrava", True), ("flygon", False)],
    },
    {
        "name": "Nincada",
        "hp": 31,
        "attack": 45,
        "defense": 90,
        "speed": 40,
        "types": ["Bug", "Ground"],
        "evolution_chain": [
            ("nincada", True),
            ("ninjask", True),
            ("ninjask", False),
            ("shedinja", False),
        ],
    },
]


def create_pokemon_instances(pokemon_data):
    pokemons = []
    for data in pokemon_data:
        pokemon = Pokemon(
            name=data["name"],
            hp=data["hp"],
            attack=data["attack"],
            defense=data["defense"],
            speed=data["speed"],
            types=data["types"],
            evolution_chain=data["evolution_chain"],
        )
        pokemons.append(pokemon)
    return pokemons


def battle_pokemon(pokemon1, pokemon2):
    battle = Battle(pokemon1, pokemon2)
    battle.start_battle()


pokemons = create_pokemon_instances(pokemon_data)


for i in range(0, len(pokemons), 2):
    pokemon1 = pokemons[i]
    pokemon2 = pokemons[i + 1] if i + 1 < len(pokemons) else None
    if pokemon2:
        print(f"Battle between {pokemon1.name} and {pokemon2.name}:")
        battle_pokemon(pokemon1, pokemon2)
        print(pokemon1)
        print(pokemon2)
        print()
