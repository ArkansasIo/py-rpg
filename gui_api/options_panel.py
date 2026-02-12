import tkinter as tk
from tkinter import ttk

class OptionsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Options / Settings").pack(anchor="nw")
        # Audio
        ttk.Label(self, text="[Audio Settings]").pack(anchor="nw")
        # Video
        ttk.Label(self, text="[Video Settings]").pack(anchor="nw")
        # Controls
        ttk.Label(self, text="[Controls Settings]").pack(anchor="nw")
