import tkinter as tk
from tkinter import ttk
from tkinter import font
# Import modular panels
from hud_panel import HUDPanel
from character_panel import CharacterPanel
from inventory_panel import InventoryPanel
from skills_panel import SkillsPanel
from quests_panel import QuestsPanel
from map_panel import MapPanel
from social_panel import SocialPanel
from achievements_panel import AchievementsPanel
from options_panel import OptionsPanel
from shop_panel import ShopPanel
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
        # Top bar (HUD)
        hud = HUDPanel(self)
        hud.pack(side="top", fill="x")

        # Left panel (navigation)
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="left", fill="y", padx=5, pady=5)
        nav_buttons = [
            ("Character", CharacterPanel),
            ("Inventory", InventoryPanel),
            ("Skills", SkillsPanel),
            ("Quests", QuestsPanel),
            ("Map", MapPanel),
            ("Social", SocialPanel),
            ("Achievements", AchievementsPanel),
            ("Options", OptionsPanel),
            ("Shop", ShopPanel)
        ]
        self.panels = {}
        for btn, panel_cls in nav_buttons:
            ttk.Button(nav_frame, text=btn, command=lambda b=btn: self.show_panel(b)).pack(fill="x", pady=2)
            self.panels[btn] = panel_cls(self.content_frame)
        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.show_panel("Character")

    # No longer needed: create_panel

    def show_panel(self, name):
        for panel in self.panels.values():
            panel.pack_forget()
        self.panels[name].pack(fill="both", expand=True)


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
