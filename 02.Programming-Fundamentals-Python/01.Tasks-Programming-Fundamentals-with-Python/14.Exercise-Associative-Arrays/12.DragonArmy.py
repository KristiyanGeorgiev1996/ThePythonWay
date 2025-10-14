n = int(input())
dragons = {}

for _ in range(n):
    type_, name, damage, health, armor = input().split()

    damage = int(damage) if damage != "null" else 45
    health = int(health) if health != "null" else 250
    armor = int(armor) if armor != "null" else 10

    if type_ not in dragons:
        dragons[type_] = {}

    # Update existing dragon or add new one
    dragons[type_][name] = {"Damage": damage, "Health": health, "Armor": armor}

for type_, dragon_dict in dragons.items():
    dragon_list = list(dragon_dict.values())
    avg_damage = sum(d['Damage'] for d in dragon_list) / len(dragon_list)
    avg_health = sum(d['Health'] for d in dragon_list) / len(dragon_list)
    avg_armor = sum(d['Armor'] for d in dragon_list) / len(dragon_list)

    print(f"{type_}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    for name in sorted(dragon_dict.keys()):
        d = dragon_dict[name]
        print(f"-{name} -> damage: {d['Damage']}, health: {d['Health']}, armor: {d['Armor']}")
