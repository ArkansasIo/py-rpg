import tkinter as tk
from tkinter import ttk

class MapPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="World Map").pack(anchor="nw")
        # Minimap and world map placeholder
        ttk.Label(self, text="[Minimap]").pack(anchor="nw")
        ttk.Label(self, text="[World Map]").pack(anchor="nw")
        ttk.Label(self, text="[Markers]").pack(anchor="nw")
