# party.py
# MMORPG party system

class Party:
    def __init__(self, leader):
        self.leader = leader
        self.members = [leader]

    def add_member(self, player):
        if player not in self.members:
            self.members.append(player)

    def remove_member(self, player):
        if player in self.members:
            self.members.remove(player)

    def is_member(self, player):
        return player in self.members
