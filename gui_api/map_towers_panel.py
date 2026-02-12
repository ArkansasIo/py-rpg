import tkinter as tk
from tkinter import ttk

class MapTowersPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Towers").pack(anchor="nw")
        for i in range(1, 6):
            ttk.Label(self, text=f"Tower {i}: [Tower Name]").pack(anchor="nw")
