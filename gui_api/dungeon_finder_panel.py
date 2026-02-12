import tkinter as tk
from tkinter import ttk

class DungeonFinderPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Dungeon Finder").pack(anchor="nw")
        ttk.Label(self, text="[Find Group for Dungeons, Raids, Trials]").pack(anchor="nw")
        ttk.Button(self, text="Find Dungeon Group").pack(anchor="nw", pady=10)
        ttk.Button(self, text="Find Raid Group").pack(anchor="nw", pady=2)
        ttk.Button(self, text="Find Trial Group").pack(anchor="nw", pady=2)