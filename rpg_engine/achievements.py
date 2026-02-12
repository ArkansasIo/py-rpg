# achievements.py
# RPG/MMORPG Achievements System

class Achievement:
    def __init__(self, name, description, unlocked=False):
        self.name = name
        self.description = description
        self.unlocked = unlocked

    def unlock(self):
        self.unlocked = True

class AchievementManager:
    def __init__(self):
        self.achievements = []

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def get_unlocked(self):
        return [a for a in self.achievements if a.unlocked]

    def get_locked(self):
        return [a for a in self.achievements if not a.unlocked]
