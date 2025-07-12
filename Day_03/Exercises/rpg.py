from abc import (ABC, abstractmethod)

class Character:
    """Template for a specific character"""

    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

# Exercise
class Mage(Character):
    def __init__(self, health=90, defense=50, magic=100):
        super().__init__(health, defense)
        self.magic =  magic

    def attack(self, other):
        damage = self.magic - other.defense

class Warrior(Character):
    def __init__(self, health=50, defense=200, strength=150):
        super().__init__(health,defense)
        self.strength = strength

    def attack(self, other):
        damage = self.strength - other.defense


knight1 = Mage()
knight2 = Warrior()
knight1.attack(knight2)

print(knight2.health)
print(knight1.health)