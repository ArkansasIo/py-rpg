
import tkinter as tk
from tkinter import ttk
from quests_act_panel import QuestsActPanel
from quests_side_panel import QuestsSidePanel

class QuestsPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
    tabs = ttk.Notebook(self)
    tabs.pack(fill="both", expand=True)
    # Acts/Chapters tab
    act_tab = QuestsActPanel(tabs)
    tabs.add(act_tab, text="Acts & Chapters")
    # Side quests tab
    side_tab = QuestsSidePanel(tabs)
    tabs.add(side_tab, text="Side Quests")
    # Placeholder for more subpages (completed, quest details)
