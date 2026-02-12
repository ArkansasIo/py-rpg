import tkinter as tk
from tkinter import ttk

class MapTrialsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Trials").pack(anchor="nw")
        for i in range(1, 6):
            ttk.Label(self, text=f"Trial {i}: [Challenge Name]").pack(anchor="nw")
