# Main Game Loop for RPG Engine
from rpg_engine.character import Character
from rpg_engine.inventory import Inventory
from rpg_engine.stats import Stats
from rpg_engine.quests import Quest
from rpg_engine.save_load import save_game_state, load_game_state
from rpg_engine.combat.combat import Combat
from rpg_engine.map.map import Map
from rpg_engine.dialogue.dialogue import Dialogue
from lib.utils import roll_dice


def main():
    print("=== RPG Adventure ===")
    # Character creation
    hero = Character("Hero", "Warrior")
    hero.stats = Stats()
    hero.inventory = Inventory()
    print(f"Character: {hero}")
    print(f"Stats: {hero.stats}")

    # Inventory
    hero.inventory.add_item("Sword")
    hero.inventory.add_item("Potion")
    print("Inventory:", hero.inventory.list_items())

    # Map
    game_map = Map(["Town", "Forest", "Dungeon"])
    game_map.show()

    # Quests
    quest1 = Quest("Find the Lost Sword", "Retrieve the sword from the dungeon.")
    print("Quest:", quest1)

    # Dialogue
    dialogue = Dialogue(["Welcome, hero!", "Your quest begins now."])
    dialogue.start()

    # Combat
    enemy = Character("Goblin", "Monster")
    enemy.stats = Stats(hp=30, strength=5)
    combat = Combat(hero, enemy)
    combat.attack()

    # Save/Load
    state = {
        "name": hero.name,
        "class": hero.char_class,
        "inventory": hero.inventory.list_items(),
        "stats": vars(hero.stats),
        "quests": [vars(quest1)],
        "location": "Town"
    }
    save_game_state(state)
    loaded_state = load_game_state()
    print("Loaded State:", loaded_state)

    print("Game setup complete. Ready for expansion!")

if __name__ == "__main__":
    main()
