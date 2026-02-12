import tkinter as tk
from tkinter import ttk

class SocialGuildPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Guild").pack(anchor="nw")
        ttk.Label(self, text="[Guild Info, Members, Ranks]").pack(anchor="nw")
