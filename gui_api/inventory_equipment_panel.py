import tkinter as tk
from tkinter import ttk

class InventoryEquipmentPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Equipment").pack(anchor="nw")
        # Equipment slots
        for slot in ["Helmet", "Armor", "Weapon", "Boots", "Ring", "Amulet"]:
            ttk.Label(self, text=f"{slot}: [Empty]").pack(anchor="nw")
