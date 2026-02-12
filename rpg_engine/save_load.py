# Save/Load logic
import json

def save_game_state(state, filename="savegame.json"):
    with open(filename, "w") as f:
        json.dump(state, f)
    print("Game state saved.")


def load_game_state(filename="savegame.json"):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        print("Game state loaded.")
        return state
    except FileNotFoundError:
        print("No save file found.")
        return None

# Add more save/load features as needed
