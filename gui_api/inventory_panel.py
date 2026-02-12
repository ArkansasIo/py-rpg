import tkinter as tk
from tkinter import ttk

class InventoryPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Inventory").pack(anchor="nw")
        # Inventory grid placeholder
        for row in range(5):
            for col in range(8):
                ttk.Label(self, text="[ ]", relief="groove", width=4).grid(row=row, column=col, padx=2, pady=2)
        # Filters and tooltips placeholder
        ttk.Label(self, text="[Filters]").pack(anchor="sw")
        ttk.Label(self, text="[Tooltip]").pack(anchor="sw")
