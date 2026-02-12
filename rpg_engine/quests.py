# Quests system
class Quest:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Active"
        return f"{self.title} ({status})"

# Add more quest features as needed
