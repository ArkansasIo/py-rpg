# pvp.py
# MMORPG PvP System

class PvPManager:
    def __init__(self):
        self.battles = []

    def start_battle(self, player1, player2):
        battle = {'player1': player1, 'player2': player2, 'status': 'active'}
        self.battles.append(battle)
        return battle

    def end_battle(self, battle, winner):
        battle['status'] = 'finished'
        battle['winner'] = winner
