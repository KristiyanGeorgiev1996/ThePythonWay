import re

class Demon:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

def calculate_health(demon_name):
    matches = re.findall(r'[^0-9+\-*/.]', demon_name)
    return sum(ord(ch) for ch in matches)

def calculate_damage(demon_name):
    damage = 0
    numbers = re.findall(r'[-+]?\d+(?:\.\d+)?', demon_name)
    for num in numbers:
        damage += float(num)
    modifiers = re.findall(r'[*\/]', demon_name)
    for mod in modifiers:
        if mod == '*':
            damage *= 2
        elif mod == '/':
            damage /= 2
    return damage

input_line = "M3ph-0.5s-0.5t0.0**"
demon_names = [d.strip() for d in re.split(r'[,\s]+', input_line) if d.strip()]

demons = [Demon(name, calculate_health(name), calculate_damage(name)) for name in demon_names]

demons.sort(key=lambda d: d.name)

for demon in demons:
    print(f"{demon.name} - {demon.health} health, {demon.damage:.2f} damage")
