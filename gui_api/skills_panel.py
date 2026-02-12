
import tkinter as tk
from tkinter import ttk
from skills_tree_panel import SkillsTreePanel

class SkillsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
    tabs = ttk.Notebook(self)
    tabs.pack(fill="both", expand=True)
    # Skill tree tab
    tree_tab = SkillsTreePanel(tabs)
    tabs.add(tree_tab, text="Skill Tree")
    # Placeholder for more subpages (active, passive, hotbar, upgrades)
