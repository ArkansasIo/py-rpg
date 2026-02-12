# economy.py
# MMORPG Economy System

class Economy:
    def __init__(self):
        self.gold = {}
        self.market = []

    def add_gold(self, player_id, amount):
        self.gold[player_id] = self.gold.get(player_id, 0) + amount

    def spend_gold(self, player_id, amount):
        if self.gold.get(player_id, 0) >= amount:
            self.gold[player_id] -= amount
            return True
        return False

    def list_item(self, item, price, seller_id):
        self.market.append({'item': item, 'price': price, 'seller': seller_id})

    def buy_item(self, item, buyer_id):
        for entry in self.market:
            if entry['item'] == item:
                if self.spend_gold(buyer_id, entry['price']):
                    self.market.remove(entry)
                    self.add_gold(entry['seller'], entry['price'])
                    return True
        return False
