# Stats system
class Stats:
    def __init__(self, hp=100, mp=50, strength=10, agility=10):
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.agility = agility

    def __str__(self):
        return f"HP: {self.hp}, MP: {self.mp}, STR: {self.strength}, AGI: {self.agility}"

# Add more stats features as needed
