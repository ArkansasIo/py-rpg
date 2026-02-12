
import tkinter as tk
from tkinter import ttk
from map_raids_panel import MapRaidsPanel
from map_trials_panel import MapTrialsPanel
from map_towers_panel import MapTowersPanel
from map_zones_panel import MapZonesPanel
from map_world_panel import MapWorldPanel
from map_dungeon_panel import MapDungeonPanel

class MapPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
    tabs = ttk.Notebook(self)
    tabs.pack(fill="both", expand=True)
    # World tab
    world_tab = MapWorldPanel(tabs)
    tabs.add(world_tab, text="World")
    # Zones tab
    zones_tab = MapZonesPanel(tabs)
    tabs.add(zones_tab, text="Zones")
    # Dungeons tab
    dungeon_tab = MapDungeonPanel(tabs)
    tabs.add(dungeon_tab, text="Dungeons")
    # Raids tab
    raids_tab = MapRaidsPanel(tabs)
    tabs.add(raids_tab, text="Raids")
    # Trials tab
    trials_tab = MapTrialsPanel(tabs)
    tabs.add(trials_tab, text="Trials")
    # Towers tab
    towers_tab = MapTowersPanel(tabs)
    tabs.add(towers_tab, text="Towers")
