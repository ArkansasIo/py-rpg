
import tkinter as tk
from tkinter import ttk
from inventory_equipment_panel import InventoryEquipmentPanel

class InventoryPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tabs = ttk.Notebook(self)
        tabs.pack(fill="both", expand=True)
        # Equipment tab
        equip_tab = InventoryEquipmentPanel(tabs)
        tabs.add(equip_tab, text="Equipment")
        # Placeholder for more subpages (consumables, crafting, quest items, cosmetics)
