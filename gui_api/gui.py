# ...existing code...
import json
import os

# Placeholder for custom font and icon support
try:
    custom_font = ("Segoe UI", 10, "bold")
except:
    custom_font = ("Arial", 10, "bold")

class RPGGUI(tk.Tk):

    def load_data(self):
        # Load config and database
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            with open(os.path.join(base, "rpg_config.json"), "r", encoding="utf-8") as f:
                self.config_data = json.load(f)
        except Exception:
            self.config_data = {}
        try:
            with open(os.path.join(base, "rpg_database_example.json"), "r", encoding="utf-8") as f:
                self.db = json.load(f)
        except Exception:
            self.db = {}

    def __init__(self):
        super().__init__()
        self.title("Eternal Horizons RPG GUI")
        self.configure(bg="#232323")
        self.geometry("1200x800")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#232323")
        self.style.configure("TLabel", background="#232323", foreground="#e0e0e0", font=custom_font)
        self.style.configure("TButton", background="#444", foreground="#e0e0e0", font=custom_font)

        self.load_data()
        self.create_main_layout()

    def create_main_layout(self):
        # Top bar
        top_frame = ttk.Frame(self)
        top_frame.pack(side="top", fill="x")
        ttk.Label(top_frame, text="Eternal Horizons | HP: 100 | MP: 50 | XP: 0", font=custom_font).pack(side="left", padx=10)

        # Left panel (navigation)
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="left", fill="y", padx=5, pady=5)
        nav_buttons = ["Character", "Quests", "Map", "Talents", "Skills", "Inventory", "Guild", "Achievements", "Social", "Options"]
        for btn in nav_buttons:
            ttk.Button(nav_frame, text=btn, command=lambda b=btn: self.show_panel(b)).pack(fill="x", pady=2)

        # Main content area
        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.panels = {}
        for panel_name in nav_buttons:
            panel = self.create_panel(panel_name)
            self.panels[panel_name] = panel
        self.show_panel("Character")

    def create_panel(self, name):
        panel = ttk.Frame(self.content_frame)
        # Example panel content
        ttk.Label(panel, text=f"{name} Panel", font=custom_font).pack(anchor="nw", pady=10)
        # Add more widgets based on panel type
        if name == "Character":
            self.character_panel(panel)
        elif name == "Inventory":
            self.inventory_panel(panel)
        elif name == "Quests":
            self.quests_panel(panel)
        elif name == "Map":
            self.map_panel(panel)
        elif name == "Talents":
            self.talents_panel(panel)
        elif name == "Skills":
            self.skills_panel(panel)
        elif name == "Guild":
            self.guild_panel(panel)
        elif name == "Achievements":
            self.achievements_panel(panel)
        elif name == "Social":
            self.social_panel(panel)
        elif name == "Options":
            self.options_panel(panel)
        return panel

    def show_panel(self, name):
        for panel in self.panels.values():
            panel.pack_forget()
        self.panels[name].pack(fill="both", expand=True)

    # Panel implementations
    def character_panel(self, panel):
        # Use first character from db
        char = self.db.get("characters", [{}])[0]
        # Tabbed sections for Character
        tabs = ttk.Notebook(panel)
        tabs.pack(fill="both", expand=True)

        # Stats Tab
        stats_tab = ttk.Frame(tabs)
        tabs.add(stats_tab, text="Stats")
        ttk.Label(stats_tab, text=f"Level: {char.get('level', 1)} {char.get('name', 'Hero')}", font=custom_font).pack(anchor="nw")
        stats = {"Strength": char.get("str", 0), "Dexterity": char.get("dex", 0), "Vitality": char.get("vit", 0)}
        for stat, value in stats.items():
            ttk.Label(stats_tab, text=f"{stat}: {value}").pack(anchor="nw")

        # Equipment Tab
        equip_tab = ttk.Frame(tabs)
        tabs.add(equip_tab, text="Equipment")
        inv = self.db.get("inventory", [])
        items = self.db.get("items", [])
        equipped = [i for i in inv if i.get("character_id") == char.get("id") and i.get("equipped")]
        ttk.Label(equip_tab, text="Equipped Items:", font=custom_font).pack(anchor="nw")
        for eq in equipped:
            item = next((it for it in items if it["id"] == eq["item_id"]), None)
            if item:
                ttk.Label(equip_tab, text=item["name"]).pack(anchor="nw")

        # Resistances Tab (placeholder)
        resist_tab = ttk.Frame(tabs)
        tabs.add(resist_tab, text="Resistances")
        resistances = {"Fire": 10, "Ice": 8, "Lightning": 5}
        for res, val in resistances.items():
            ttk.Label(resist_tab, text=f"{res}: {val}").pack(anchor="nw")

    def inventory_panel(self, panel):
        char = self.db.get("characters", [{}])[0]
        inv = self.db.get("inventory", [])
        items = self.db.get("items", [])
        # Tabbed sections for Inventory
        tabs = ttk.Notebook(panel)
        tabs.pack(fill="both", expand=True)

        # Items Tab
        items_tab = ttk.Frame(tabs)
        tabs.add(items_tab, text="Items")
        ttk.Label(items_tab, text="Inventory Items:", font=custom_font).pack(anchor="nw")
        item_grid = ttk.Frame(items_tab)
        item_grid.pack(anchor="nw")
        char_inv = [i for i in inv if i.get("character_id") == char.get("id")]
        for idx, inv_item in enumerate(char_inv):
            item = next((it for it in items if it["id"] == inv_item["item_id"]), None)
            if item:
                label = f"{item['name']} x{inv_item['quantity']}"
                ttk.Label(item_grid, text=label, relief="groove", width=20).grid(row=idx//3, column=idx%3, padx=5, pady=5)

        # Currency Tab (placeholder)
        currency_tab = ttk.Frame(tabs)
        tabs.add(currency_tab, text="Currency")
        ttk.Label(currency_tab, text="Gold: 257", font=custom_font).pack(anchor="nw")
        ttk.Label(currency_tab, text="Silver: 78").pack(anchor="nw")

        # Parts Tab (placeholder)
        parts_tab = ttk.Frame(tabs)
        tabs.add(parts_tab, text="Parts")
        parts = ["Relic Fragment", "Ancient Scroll"]
        ttk.Label(parts_tab, text="Parts:", font=custom_font).pack(anchor="nw")
        for part in parts:
            ttk.Label(parts_tab, text=part).pack(anchor="nw")

    def quests_panel(self, panel):
        ttk.Label(panel, text="Active Quests:").pack(anchor="nw")
        quests = ["Defeat Goblin Leader", "Retrieve Ancient Relic"]
        for quest in quests:
            ttk.Label(panel, text=quest).pack(anchor="nw")

    def map_panel(self, panel):
        ttk.Label(panel, text="World Map:").pack(anchor="nw")
        ttk.Label(panel, text="[Map Placeholder]").pack(anchor="nw")

    def talents_panel(self, panel):
        ttk.Label(panel, text="Talent Tree:").pack(anchor="nw")
        ttk.Label(panel, text="[Talent Tree Placeholder]").pack(anchor="nw")

    def skills_panel(self, panel):
        ttk.Label(panel, text="Skills:").pack(anchor="nw")
        skills = ["Slash", "Fireball", "Heal"]
        for skill in skills:
            ttk.Label(panel, text=skill).pack(anchor="nw")

    def guild_panel(self, panel):
        ttk.Label(panel, text="Guild Members:").pack(anchor="nw")
        members = ["Leader: Golaf", "Member: Otti", "Member: Galila"]
        for member in members:
            ttk.Label(panel, text=member).pack(anchor="nw")

    def achievements_panel(self, panel):
        ttk.Label(panel, text="Achievements:").pack(anchor="nw")
        achievements = self.db.get("achievements", [])
        if not achievements:
            # Fallback to static if not in db
            achievements = [
                {"name": "First Blood", "description": "Defeat your first enemy.", "unlocked": True},
                {"name": "Master Explorer", "description": "Discover all zones.", "unlocked": False}
            ]
        for ach in achievements:
            status = "[Unlocked]" if ach.get("unlocked") else "[Locked]"
            text = f"{ach.get('name', 'Achievement')}: {ach.get('description', '')} {status}"
            ttk.Label(panel, text=text).pack(anchor="nw")

    def social_panel(self, panel):
        ttk.Label(panel, text="Chat:").pack(anchor="nw")
        ttk.Label(panel, text="[Chat Placeholder]").pack(anchor="nw")

    def options_panel(self, panel):
        ttk.Label(panel, text="Settings:").pack(anchor="nw")
        ttk.Button(panel, text="Audio").pack(anchor="nw")
        ttk.Button(panel, text="Graphics").pack(anchor="nw")
        ttk.Button(panel, text="Controls").pack(anchor="nw")

if __name__ == "__main__":
    gui = RPGGUI()
    gui.mainloop()
# GUI API
# Entry point for GUI logic


def show_title_page(title):
    print(f"=== {title} ===")

def show_splash_screen(message):
    print(f"--- {message} ---")

def show_loading_screen(message="Loading..."):
    print(f"*** {message} ***")

def show_main_menu(options=None):
    print("Main Menu")
    if options:
        for option in options:
            print(f"- {option}")

# Example usage
if __name__ == "__main__":
    show_title_page("RPG Adventure")
    show_splash_screen("Welcome to the RPG!")
    show_loading_screen()
    show_main_menu([
        "Character Creation",
        "New Game",
        "Continue",
        "Load Game",
        "Inventory",
        "Stats",
        "Settings"
    ])
