# Full RPG/MMORPG Stat, Combat, and Itemization System
# (Production-grade, PvE/PvP, Boss, Mob, AI, Scaling, Loot, Data Schemas)

# 1. Core Attributes
CORE_ATTRIBUTES = [
    "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Vitality", "Spirit", "Luck", "Willpower", "Charisma"
]

# 2. Sub-Attributes
SUB_ATTRIBUTES = [
    # Physical
    "Physical Power", "Armor Penetration", "Attack Speed", "Accuracy", "Evasion", "Crit Damage", "Weapon Mastery",
    # Magical
    "Spell Power", "Elemental Mastery", "Cast Speed", "Magic Penetration", "Mana Efficiency", "Overcharge", "Healing Power",
    # Survival
    "Max HP", "HP Regen", "Shield Strength", "Damage Reduction", "Block Chance", "Parry Chance", "Tenacity", "Poise"
]

# 3. Combat Stats
COMBAT_STATS = [
    # Offense
    "Base Attack", "Skill Power %", "Crit Chance", "Crit Damage", "Vulnerability Damage %", "Backstab Multiplier", "DoT Power", "Execute Damage %",
    # Defense
    "Armor", "Magic Resistance", "Mitigation %", "Block Value", "Parry Window", "Dodge Chance", "Damage Taken Modifiers",
    # Tempo
    "Move Speed", "Attack Speed", "Cast Speed", "Cooldown Reduction", "Global Cooldown", "Resource Regen"
]

# 4. Resources
RESOURCES = [
    "HP", "MP", "Stamina", "Energy", "Rage", "Focus", "Faith", "Aether", "Heat", "Sanity"
]

# 5. Damage Types & Resistances
DAMAGE_TYPES = [
    "Physical", "Fire", "Ice", "Lightning", "Earth", "Wind", "Water", "Light", "Dark", "Arcane", "Poison", "Bleed", "Void", "Chaos", "True"
]
RESISTANCE_TYPES = [
    "Flat", "Percent", "Absorption", "Immunity", "Vulnerability"
]

# 6. Buffs & Debuffs
BUFFS = [
    "Power Surge", "Berserk", "Arcane Amplify", "Precision", "Shielded", "Fortified", "Regeneration", "Haste", "Stealth", "Flight", "Invisibility", "True Sight", "Phase Shift"
]
DEBUFFS = [
    "Stun", "Freeze", "Root", "Silence", "Fear", "Charm", "Sleep", "Knockback", "Burn", "Poison", "Bleed", "Corruption", "Frostbite", "Shock", "Weakness", "Frailty", "Hex", "Slow", "Cripple", "Curse"
]

# 7. Enemy & Boss Types
ENEMY_TIERS = [
    "Trash Mob", "Veteran", "Elite", "Champion", "Dungeon Boss", "World Boss", "Raid Boss", "Mythic", "Ascended"
]
AI_ARCHETYPES = [
    "Brute", "Assassin", "Caster", "Controller", "Summoner", "Support", "Tank", "Sniper"
]

# 8. PvE & PvP Equipment
WEAPON_TYPES = [
    "Greatsword", "Longsword", "Axe", "Mace", "Spear", "Dagger", "Fist", "Scythe", "Bow", "Crossbow", "Gun", "Throwing", "Staff", "Wand", "Tome", "Catalyst", "Relic"
]
ARMOR_TYPES = ["Light", "Medium", "Heavy"]
ACCESSORY_TYPES = ["Ring", "Amulet", "Cloak", "Belt", "Trinket"]
RARITIES = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic"]

# 9. Item Data Schema Example
ITEM_SCHEMA = {
    "name": "",
    "type": "Weapon/Armor/Trinket",
    "slot": "",
    "rarity": "",
    "pve_stats": {},
    "pvp_stats": {},
    "set_bonus": {},
    "enchantments": [],
    "required_level": 1,
    "bind_rules": "",
    "cosmetic": {}
}

# 10. Stat Value Formula (for balancing)
def stat_value_pu(raw_stat, stat_weight, scaling_curve=1.0):
    return raw_stat * stat_weight * scaling_curve

# 11. Weapon Power Formula (PvE/PvP)
def weapon_power_pve(base_damage, weapon_speed, main_stat, stat_coef, element_damage, element_coef, pve_mult=1.0):
    return (base_damage * weapon_speed + main_stat * stat_coef + element_damage * element_coef) * pve_mult

def weapon_power_pvp(normalized_base, main_stat, pvp_stat_scale, pvp_dampening=0.8):
    return (normalized_base + main_stat * pvp_stat_scale) * pvp_dampening

# 12. Armor Mitigation Formula
def damage_mitigation(armor, k, attacker_level):
    return armor / (armor + k * attacker_level)

# 13. Item Power Formula
def item_power(stat_values, proc_value=0, set_bonus_value=0):
    return sum(stat_values) + proc_value + set_bonus_value

# 14. Buff/Debuff Value Formula
def buff_value(stat_increase, duration, target_count, context_mult=1.0):
    return stat_increase * duration * target_count * context_mult

# 15. Boss Scaling Formula
def boss_hp(base_hp, level_diff, party_mult, diff_mult):
    return base_hp * (1 + level_diff * 0.18) * party_mult * diff_mult

def boss_damage(base_dmg, level_diff, diff_mult):
    return base_dmg * (1 + level_diff * 0.12) * diff_mult

# 16. Encounter Power Budget
def encounter_power_budget(player_power, difficulty_factor):
    return sum(player_power) * difficulty_factor

# 17. Hard Caps
HARD_CAPS = {
    "Crit Chance PvP": 0.4,
    "Crit Chance PvE": 0.7,
    "CDR PvP": 0.35,
    "CDR PvE": 0.6,
    "CC Duration PvP": 0.5,
    "Damage Reduction": 0.7,
    "Healing Bonus PvP": 0.5
}

# 18. Example: Full Item Data
EXAMPLE_ITEM = {
    "name": "Ashen Blade",
    "type": "Weapon",
    "slot": "Main Hand",
    "rarity": "Epic",
    "pve_stats": {
        "attack": 1200,
        "fire_damage": 15,
        "crit_chance": 5,
        "boss_damage": 10,
        "proc": "Burn on hit"
    },
    "pvp_stats": {
        "attack": 650,
        "pvp_power": 10,
        "anti_heal": 20,
        "burn_cap": True
    }
}

# 19. Boss Data Schema
BOSS_SCHEMA = {
    "name": "",
    "rank": "",
    "level": 1,
    "hp": 100000,
    "phases": [],
    "abilities": [],
    "immunities": [],
    "affixes": [],
    "loot_table": [],
    "enrage_timer": 0,
    "ai_profile": "",
    "arena_rules": {}
}

# 20. PvE/PvP Separation Example
# PvE and PvP stats are always separated for balance.
# Use pve_stats and pvp_stats in all item, ability, and effect data.

# This file can be imported and extended for any RPG/MMORPG project.
