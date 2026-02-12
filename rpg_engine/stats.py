# Core and sub stats for RPG/MMORPG
CORE_STATS = [
    "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"
]

SUB_STATS = [
    "HP", "MP", "Stamina", "Attack Power", "Spell Power", "Armor", "Evasion", "Crit Chance", "Crit Damage", "Haste", "Block", "Resist Fire", "Resist Ice", "Resist Lightning", "Resist Poison", "Resist Holy", "Resist Dark"
]

# Example stat groups by class type
CLASS_STAT_PRIORITIES = {
    "Barbarian": ["Strength", "Constitution", "HP", "Attack Power"],
    "Bard": ["Charisma", "Dexterity", "MP", "Spell Power"],
    "Cleric": ["Wisdom", "Constitution", "MP", "Resist Holy"],
    "Druid": ["Wisdom", "Intelligence", "MP", "Resist Poison"],
    "Fighter": ["Strength", "Dexterity", "HP", "Armor"],
    "Monk": ["Dexterity", "Wisdom", "Stamina", "Evasion"],
    "Paladin": ["Strength", "Charisma", "HP", "Block"],
    "Ranger": ["Dexterity", "Wisdom", "Stamina", "Crit Chance"],
    "Rogue": ["Dexterity", "Charisma", "Crit Chance", "Evasion"]
}

# Example: Stat types
STAT_TYPES = ["Physical", "Magical", "Defensive", "Utility", "Elemental"]

# Example: Buff/debuff stat effects
BUFFABLE_STATS = ["Strength", "Dexterity", "HP", "MP", "Attack Power", "Armor", "Crit Chance", "Haste"]
DEBUFFABLE_STATS = ["Strength", "Dexterity", "HP", "MP", "Armor", "Evasion", "Resistances"]

# Stats system class (example)
class Stats:
    def __init__(self, hp=100, mp=50, strength=10, agility=10):
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.agility = agility

    def __str__(self):
        return f"HP: {self.hp}, MP: {self.mp}, STR: {self.strength}, AGI: {self.agility}"
