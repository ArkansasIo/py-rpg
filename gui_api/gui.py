# GUI API
# Entry point for GUI logic


def show_title_page(title):
    print(f"=== {title} ===")

def show_splash_screen(message):
    print(f"--- {message} ---")

def show_loading_screen(message="Loading..."):
    print(f"*** {message} ***")

def show_main_menu(options=None):
    print("Main Menu")
    if options:
        for option in options:
            print(f"- {option}")

# Example usage
if __name__ == "__main__":
    show_title_page("RPG Adventure")
    show_splash_screen("Welcome to the RPG!")
    show_loading_screen()
    show_main_menu([
        "Character Creation",
        "New Game",
        "Continue",
        "Load Game",
        "Inventory",
        "Stats",
        "Settings"
    ])
