# RPG Engine API
# Entry point for RPG game logic

class Menu:
    def __init__(self, name, submenus=None):
        self.name = name
        self.submenus = submenus or []

    def display(self):
        print(f"Menu: {self.name}")
        for submenu in self.submenus:
            submenu.display()



class TitlePage:
    def __init__(self, title):
        self.title = title

    def show(self):
        print(f"=== {self.title} ===")

class SplashScreen:
    def __init__(self, message):
        self.message = message

    def show(self):
        print(f"--- {self.message} ---")

class LoadingScreen:
    def __init__(self, message="Loading..."):
        self.message = message

    def show(self):
        print(f"*** {self.message} ***")

class Page:
    def __init__(self, title, subpages=None):
        self.title = title
        self.subpages = subpages or []

    def show(self):
        print(f"Page: {self.title}")
        for subpage in self.subpages:
            subpage.show()



# Example screens
title_page = TitlePage("RPG Adventure")
splash_screen = SplashScreen("Welcome to the RPG!")
loading_screen = LoadingScreen()

# Expanded main menu
main_menu = Menu("Main Menu", [
    Menu("Character Creation"),
    Menu("New Game"),
    Menu("Continue"),
    Menu("Load Game"),
    Menu("Inventory"),
    Menu("Stats"),
    Menu("Settings")
])

# Example main page
main_page = Page("Home", [Page("Profile"), Page("Quests"), Page("Map")])

# Game logic placeholder

class RPGGame:
    def __init__(self):
        self.title_page = title_page
        self.splash_screen = splash_screen
        self.loading_screen = loading_screen
        self.menu = main_menu
        self.page = main_page

    def start(self):
        self.title_page.show()
        self.splash_screen.show()
        self.loading_screen.show()
        print("Starting RPG Game...")
        self.menu.display()
        self.page.show()

# Add more RPG features as needed
