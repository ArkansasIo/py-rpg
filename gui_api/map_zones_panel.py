
import tkinter as tk
from tkinter import ttk

class MapZonesPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Zones").pack(anchor="nw")
        for i in range(1, 73):
            ttk.Label(self, text=f"Zone {i}: [Zone Name]").pack(anchor="nw")
            # Example sub-zones for each zone
            for sub in range(1, 4):
                ttk.Label(self, text=f"   Sub-zone {sub}: [Sub-zone Name]").pack(anchor="nw")
