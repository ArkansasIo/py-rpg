import tkinter as tk
from tkinter import ttk

class SkillsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text="Skills & Talents").pack(anchor="nw")
        # Skill tree placeholder
        ttk.Label(self, text="[Skill Tree]").pack(anchor="nw")
        # Hotbar placeholder
        ttk.Label(self, text="[Skill Hotbar]").pack(anchor="nw")
