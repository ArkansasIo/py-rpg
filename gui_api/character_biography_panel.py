import tkinter as tk
from tkinter import ttk

class CharacterBiographyPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Biography").pack(anchor="nw")
        ttk.Label(self, text="[Character Story, Origin, etc.]").pack(anchor="nw")
