# world.py
# MMORPG World/Map System

class World:
    def __init__(self):
        self.zones = []
        self.events = []

    def add_zone(self, name, description):
        self.zones.append({'name': name, 'description': description})

    def add_event(self, event):
        self.events.append(event)

    def get_zones(self):
        return self.zones

    def get_events(self):
        return self.events
