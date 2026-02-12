import tkinter as tk
from tkinter import ttk

class ShopPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Shop / Trading / Auction").pack(anchor="nw")
        # Shop
        ttk.Label(self, text="[Shop Items]").pack(anchor="nw")
        # Trading
        ttk.Label(self, text="[Trading Window]").pack(anchor="nw")
        # Auction
        ttk.Label(self, text="[Auction House]").pack(anchor="nw")
