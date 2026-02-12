# PvE/PvP Stat Separation Schema

## Principle
All items, abilities, and effects must have separate PvE and PvP stats for balance.

## Example (JSON)
```
{
  "name": "Ashen Blade",
  "type": "Weapon",
  "pve_stats": {"attack": 1200, "fire_damage": 15, "crit_chance": 5, "boss_damage": 10},
  "pvp_stats": {"attack": 650, "pvp_power": 10, "anti_heal": 20}
}
```

## Usage
- Always reference both pve_stats and pvp_stats in item, ability, and effect data.
- PvP stats may include dampening, anti-heal, CC duration, etc.
- PvE stats may include boss damage, mob damage, proc effects, etc.

## Rationale
- Ensures fair and fun gameplay in both modes.
- Allows for independent balancing.
