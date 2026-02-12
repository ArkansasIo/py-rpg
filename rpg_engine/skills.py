# skills.py
# RPG skill system

class Skill:
    def __init__(self, name, description, power, cost, cooldown):
        self.name = name
        self.description = description
        self.power = power
        self.cost = cost
        self.cooldown = cooldown
        self.current_cooldown = 0

    def use(self, user, target):
        if self.current_cooldown > 0:
            return False, f"Skill {self.name} is on cooldown."
        # Example skill effect
        target.stats['hp'] -= self.power
        self.current_cooldown = self.cooldown
        return True, f"{user.name} used {self.name} on {target.name}!"

    def tick(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1

class SkillTree:
    def __init__(self):
        self.skills = {}

    def add_skill(self, skill):
        self.skills[skill.name] = skill

    def get_skill(self, name):
        return self.skills.get(name)
