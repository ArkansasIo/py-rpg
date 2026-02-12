
import tkinter as tk
from tkinter import ttk
from character_attributes_panel import CharacterAttributesPanel
from character_biography_panel import CharacterBiographyPanel

class CharacterPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tabs = ttk.Notebook(self)
        tabs.pack(fill="both", expand=True)
        # Attributes tab
        attr_tab = CharacterAttributesPanel(tabs)
        tabs.add(attr_tab, text="Attributes")
        # Biography tab
        bio_tab = CharacterBiographyPanel(tabs)
        tabs.add(bio_tab, text="Biography")
        # Placeholder for more subpages (reputation, appearance, mounts, pets)
        ttk.Label(self, text="[Character Portrait]").pack(anchor="nw")
