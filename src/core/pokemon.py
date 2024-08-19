class Pokemon:
    def __init__(
        self,
        name: str,
        hp: int,
        attack: int,
        defense: int,
        speed: int,
        types: list[str],
        evolution_chain: list[tuple],
    ):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.types = types
        self.evolution_chain = evolution_chain
        self.points = 0

    POINTS_TO_EVOLVE = 200

    def can_evolve(self) -> bool:
        if self.points >= self.POINTS_TO_EVOLVE and self.evolution_chain:
            matching_evolution = next(
                (evolution for evolution in self.evolution_chain if evolution[0] == self.name.lower()),
                None
            )
            if matching_evolution:
                return matching_evolution[1]
        return False

    def evolve(self):
        for i, (next_evolution, can_evolve_by_level) in enumerate(self.evolution_chain):
            if self.name.lower() == next_evolution:
                if can_evolve_by_level and self.points >= self.POINTS_TO_EVOLVE:
                    if i + 1 < len(self.evolution_chain):
                        self.name = self.evolution_chain[i + 1][0].capitalize()
                        self.points -= self.POINTS_TO_EVOLVE
                        break
                break

    def receive_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def calculate_damage(self, attack_types: list[str], opponent: 'Pokemon') -> int:
        from battle import TypeEffectiveness
        effectiveness = TypeEffectiveness(attack_types, opponent.types).calculate_effectiveness()

        base_damage = self.attack * effectiveness
        reduced_damage = base_damage - (0.3 * opponent.defense)

        min_damage = 1 if effectiveness > 0 else 0

        damage = max(min_damage, int(reduced_damage))
        return damage

    def gain_experience(self, points: int):
        self.points += points

    def get_name(self):
        return self.name

    def __str__(self):
        return f"""
            {self.name}
            | HP: {self.hp} | Ataque: {self.attack} | Defensa: {self.defense} | Velocidad: {self.speed} | Tipos: {self.types}
        """
