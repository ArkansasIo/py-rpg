import tkinter as tk
from tkinter import ttk

class CharacterPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Character Sheet").pack(anchor="nw")
        # Stats
        stats = ["Strength", "Dexterity", "Vitality", "Intelligence", "Luck"]
        for stat in stats:
            ttk.Label(self, text=f"{stat}: 10").pack(anchor="nw")
        # Equipment slots
        ttk.Label(self, text="[Equipment Slots]").pack(anchor="nw")
        # Appearance placeholder
        ttk.Label(self, text="[Character Portrait]").pack(anchor="nw")
