class TypeEffectiveness:

    effectiveness_chart = {
        # Super effective (2x)
        ("Fire", "Grass"): 2,
        ("Fire", "Ice"): 2,
        ("Fire", "Bug"): 2,
        ("Fire", "Steel"): 2,
        ("Water", "Fire"): 2,
        ("Water", "Ground"): 2,
        ("Water", "Rock"): 2,
        ("Electric", "Water"): 2,
        ("Electric", "Flying"): 2,
        ("Grass", "Water"): 2,
        ("Grass", "Ground"): 2,
        ("Grass", "Rock"): 2,
        ("Ice", "Grass"): 2,
        ("Ice", "Ground"): 2,
        ("Ice", "Flying"): 2,
        ("Ice", "Dragon"): 2,
        ("Fighting", "Normal"): 2,
        ("Fighting", "Ice"): 2,
        ("Fighting", "Rock"): 2,
        ("Fighting", "Dark"): 2,
        ("Fighting", "Steel"): 2,
        ("Poison", "Grass"): 2,
        ("Ground", "Fire"): 2,
        ("Ground", "Electric"): 2,
        ("Ground", "Poison"): 2,
        ("Ground", "Rock"): 2,
        ("Ground", "Steel"): 2,
        ("Flying", "Grass"): 2,
        ("Flying", "Fighting"): 2,
        ("Flying", "Bug"): 2,
        ("Psychic", "Fighting"): 2,
        ("Psychic", "Poison"): 2,
        ("Bug", "Grass"): 2,
        ("Bug", "Psychic"): 2,
        ("Bug", "Dark"): 2,
        ("Rock", "Fire"): 2,
        ("Rock", "Ice"): 2,
        ("Rock", "Flying"): 2,
        ("Rock", "Bug"): 2,
        ("Ghost", "Psychic"): 2,
        ("Ghost", "Ghost"): 2,
        ("Dragon", "Dragon"): 2,
        ("Dark", "Psychic"): 2,
        ("Dark", "Ghost"): 2,
        ("Steel", "Ice"): 2,
        ("Steel", "Rock"): 2,
        ("Fairy", "Fighting"): 2,
        ("Fairy", "Dragon"): 2,
        ("Fairy", "Dark"): 2,
        # Not very effective (0.5x)
        ("Fire", "Fire"): 0.5,
        ("Fire", "Water"): 0.5,
        ("Fire", "Rock"): 0.5,
        ("Fire", "Dragon"): 0.5,
        ("Water", "Water"): 0.5,
        ("Water", "Grass"): 0.5,
        ("Water", "Dragon"): 0.5,
        ("Electric", "Electric"): 0.5,
        ("Electric", "Grass"): 0.5,
        ("Electric", "Dragon"): 0.5,
        ("Grass", "Fire"): 0.5,
        ("Grass", "Grass"): 0.5,
        ("Grass", "Poison"): 0.5,
        ("Grass", "Flying"): 0.5,
        ("Grass", "Bug"): 0.5,
        ("Grass", "Dragon"): 0.5,
        ("Grass", "Steel"): 0.5,
        ("Ice", "Fire"): 0.5,
        ("Ice", "Water"): 0.5,
        ("Ice", "Ice"): 0.5,
        ("Ice", "Steel"): 0.5,
        ("Fighting", "Poison"): 0.5,
        ("Fighting", "Flying"): 0.5,
        ("Fighting", "Psychic"): 0.5,
        ("Fighting", "Bug"): 0.5,
        ("Fighting", "Fairy"): 0.5,
        ("Poison", "Poison"): 0.5,
        ("Poison", "Ground"): 0.5,
        ("Poison", "Rock"): 0.5,
        ("Poison", "Ghost"): 0.5,
        ("Ground", "Grass"): 0.5,
        ("Ground", "Bug"): 0.5,
        ("Flying", "Electric"): 0.5,
        ("Flying", "Rock"): 0.5,
        ("Flying", "Steel"): 0.5,
        ("Psychic", "Psychic"): 0.5,
        ("Psychic", "Steel"): 0.5,
        ("Bug", "Fire"): 0.5,
        ("Bug", "Fighting"): 0.5,
        ("Bug", "Poison"): 0.5,
        ("Bug", "Flying"): 0.5,
        ("Bug", "Ghost"): 0.5,
        ("Bug", "Steel"): 0.5,
        ("Bug", "Fairy"): 0.5,
        ("Rock", "Fighting"): 0.5,
        ("Rock", "Ground"): 0.5,
        ("Rock", "Steel"): 0.5,
        ("Ghost", "Dark"): 0.5,
        ("Dragon", "Steel"): 0.5,
        ("Dark", "Fighting"): 0.5,
        ("Dark", "Dark"): 0.5,
        ("Dark", "Fairy"): 0.5,
        ("Steel", "Fire"): 0.5,
        ("Steel", "Water"): 0.5,
        ("Steel", "Electric"): 0.5,
        ("Steel", "Steel"): 0.5,
        ("Fairy", "Fire"): 0.5,
        ("Fairy", "Poison"): 0.5,
        ("Fairy", "Steel"): 0.5,
        # Immune
        ("Electric", "Ground"): 0,
        ("Fight", "Ghost"): 0,
        ("Ground", "Flying"): 0,
        ("Normal", "Ghost"): 0,
        ("Poison", "Steel"): 0,
        ("Psychic", "Dark"): 0,
        ("Dragon", "Fairy"): 0,
    }

    def __init__(self, attack_types: list[str], defense_types: list[str]):
        self.attack_types = attack_types
        self.defense_types = defense_types

    def calculate_effectiveness(self) -> float:
        max_effectiveness = 0

        for attack_type in self.attack_types:
            effectiveness = 1
            for defense_type in self.defense_types:
                effectiveness *= TypeEffectiveness.effectiveness_chart.get(
                    (attack_type, defense_type), 1
                )
            max_effectiveness = max(max_effectiveness, effectiveness)

        return max_effectiveness
