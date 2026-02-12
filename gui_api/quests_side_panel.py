import tkinter as tk
from tkinter import ttk

class QuestsSidePanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Side Quests").pack(anchor="nw")
        for i in range(1, 11):
            ttk.Label(self, text=f"Side Quest {i}").pack(anchor="nw")
