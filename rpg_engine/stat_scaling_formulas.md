# Stat Scaling & Combat Formulas

## Stat Value Calculation
- **Stat Value**: `raw_stat * stat_weight * scaling_curve`
- **Weapon Power (PvE)**: `(base_damage * weapon_speed + main_stat * stat_coef + element_damage * element_coef) * pve_mult`
- **Weapon Power (PvP)**: `(normalized_base + main_stat * pvp_stat_scale) * pvp_dampening`
- **Armor Mitigation**: `armor / (armor + k * attacker_level)`
- **Item Power**: `sum(stat_values) + proc_value + set_bonus_value`
- **Buff Value**: `stat_increase * duration * target_count * context_mult`
- **Boss HP Scaling**: `base_hp * (1 + level_diff * 0.18) * party_mult * diff_mult`
- **Boss Damage Scaling**: `base_dmg * (1 + level_diff * 0.12) * diff_mult`
- **Encounter Power Budget**: `sum(player_power) * difficulty_factor`

## Hard Caps
- Crit Chance PvP: 40%
- Crit Chance PvE: 70%
- CDR PvP: 35%
- CDR PvE: 60%
- CC Duration PvP: 50%
- Damage Reduction: 70%
- Healing Bonus PvP: 50%

## PvE/PvP Separation
- All items, abilities, and effects have separate PvE and PvP stats for balance.

## Example Data Schemas
- See stat_system_full.py for full schemas and formulas.
