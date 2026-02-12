import tkinter as tk
from tkinter import ttk

class AchievementsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Achievements / Codex").pack(anchor="nw")
        # Achievements
        ttk.Label(self, text="[Achievements List]").pack(anchor="nw")
        # Codex
        ttk.Label(self, text="[Codex Entries]").pack(anchor="nw")
