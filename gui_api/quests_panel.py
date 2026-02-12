import tkinter as tk
from tkinter import ttk

class QuestsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Quests / Journal").pack(anchor="nw")
        # Active quests
        ttk.Label(self, text="[Active Quests]").pack(anchor="nw")
        # Completed quests
        ttk.Label(self, text="[Completed Quests]").pack(anchor="nw")
        # Quest details placeholder
        ttk.Label(self, text="[Quest Details]").pack(anchor="nw")
