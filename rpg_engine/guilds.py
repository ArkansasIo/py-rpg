# guilds.py
# MMORPG guild system

class Guild:
    def __init__(self, name, leader):
        self.name = name
        self.leader = leader
        self.members = [leader]
        self.bank = {}

    def add_member(self, player):
        if player not in self.members:
            self.members.append(player)

    def remove_member(self, player):
        if player in self.members:
            self.members.remove(player)

    def deposit(self, item, amount):
        self.bank[item] = self.bank.get(item, 0) + amount

    def withdraw(self, item, amount):
        if self.bank.get(item, 0) >= amount:
            self.bank[item] -= amount
            return True
        return False
