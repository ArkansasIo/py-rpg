import tkinter as tk
from tkinter import ttk

class CharacterAttributesPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Attributes").pack(anchor="nw")
        # Strength, Dexterity, etc.
        for stat in ["Strength", "Dexterity", "Vitality", "Intelligence", "Luck"]:
            ttk.Label(self, text=f"{stat}: 10").pack(anchor="nw")
