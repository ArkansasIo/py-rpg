import tkinter as tk
from tkinter import ttk

class HUDPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Health, Mana, XP bars
        ttk.Label(self, text="HP: 100 / 100").pack(anchor="w")
        ttk.Label(self, text="MP: 50 / 50").pack(anchor="w")
        ttk.Label(self, text="XP: 0 / 1000").pack(anchor="w")
        # Minimap placeholder
        ttk.Label(self, text="[Minimap]").pack(anchor="e")
        # Quickbar placeholder
        ttk.Label(self, text="[Quickbar]").pack(anchor="s")
