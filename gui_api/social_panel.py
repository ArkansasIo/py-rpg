import tkinter as tk
from tkinter import ttk

class SocialPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Social").pack(anchor="nw")
        # Chat
        ttk.Label(self, text="[Chat Window]").pack(anchor="nw")
        # Friends
        ttk.Label(self, text="[Friends List]").pack(anchor="nw")
        # Guild
        ttk.Label(self, text="[Guild Info]").pack(anchor="nw")
        # Party
        ttk.Label(self, text="[Party Info]").pack(anchor="nw")
