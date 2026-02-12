import tkinter as tk
from tkinter import ttk

class AchievementsCodexPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Codex").pack(anchor="nw")
        ttk.Label(self, text="[Lore, Bestiary, World Info]").pack(anchor="nw")
