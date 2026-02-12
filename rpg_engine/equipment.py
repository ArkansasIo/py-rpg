# equipment.py
# RPG equipment system

class Equipment:
    def __init__(self, name, slot, stats):
        self.name = name
        self.slot = slot  # e.g. 'head', 'body', 'weapon'
        self.stats = stats  # dict of stat bonuses

class EquipmentManager:
    def __init__(self):
        self.equipped = {}

    def equip(self, equipment):
        self.equipped[equipment.slot] = equipment

    def unequip(self, slot):
        return self.equipped.pop(slot, None)

    def get_total_stats(self):
        total = {}
        for eq in self.equipped.values():
            for stat, value in eq.stats.items():
                total[stat] = total.get(stat, 0) + value
        return total
