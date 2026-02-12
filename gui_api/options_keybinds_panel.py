import tkinter as tk
from tkinter import ttk

class OptionsKeybindsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Keybinds").pack(anchor="nw")
        ttk.Label(self, text="[Keybinding Settings Placeholder]").pack(anchor="nw")
