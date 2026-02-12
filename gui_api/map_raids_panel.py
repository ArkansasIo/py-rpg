import tkinter as tk
from tkinter import ttk

class MapRaidsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Raids").pack(anchor="nw")
        for i in range(1, 6):
            ttk.Label(self, text=f"Raid {i}: [Boss Name]").pack(anchor="nw")
