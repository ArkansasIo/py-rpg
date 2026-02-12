import tkinter as tk
from tkinter import ttk

class QuestsActPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Acts & Chapters").pack(anchor="nw")
        for act in range(1, 6):
            ttk.Label(self, text=f"Act {act}").pack(anchor="nw")
            for chapter in range(1, 11):
                ttk.Label(self, text=f"  Chapter {chapter}").pack(anchor="nw")
