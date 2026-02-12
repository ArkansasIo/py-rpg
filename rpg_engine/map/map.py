# Map system
class Map:
    def __init__(self, locations=None):
        self.locations = locations or []

    def show(self):
        print("Map:")
        for loc in self.locations:
            print(f"- {loc}")

# Add more map features as needed
