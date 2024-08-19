import random
from core import Pokemon


class Battle:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def decide_first_attacker(self):
        if self.pokemon1.speed > self.pokemon2.speed:
            return self.pokemon1, self.pokemon2
        elif self.pokemon1.speed < self.pokemon2.speed:
            return self.pokemon2, self.pokemon1
        else:
            return random.choice([(self.pokemon1, self.pokemon2), (self.pokemon2, self.pokemon1)])

    def perform_attack(self, attacker: Pokemon, defender: Pokemon):
        damage = attacker.calculate_damage(attacker.types, defender)
        defender.receive_damage(damage)
        print(f"{attacker.name} attacks {defender.name} for {damage} damage!")
        print(f"{defender.name} has {defender.hp} HP remaining.")

    def start_battle(self):
        print("Battle begins!")
        attacker, defender = self.decide_first_attacker()

        self.perform_attack(attacker, defender)
        if defender.hp > 0:
            self.perform_attack(defender, attacker)

        if self.pokemon1.hp > 0 and self.pokemon2.hp <= 0:
            print(f"{self.pokemon1.name} wins!")
        elif self.pokemon2.hp > 0 and self.pokemon1.hp <= 0:
            print(f"{self.pokemon2.name} wins!")
        elif self.pokemon1.hp > self.pokemon2.hp:
            print(f"{self.pokemon1.name} wins by having more HP!")
        elif self.pokemon2.hp > self.pokemon1.hp:
            print(f"{self.pokemon2.name} wins by having more HP!")
        else:
            print("It's a draw!")
