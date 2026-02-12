import tkinter as tk
from tkinter import ttk

class MapWorldPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="World").pack(anchor="nw")
        ttk.Label(self, text="[World Map Overview]").pack(anchor="nw")
