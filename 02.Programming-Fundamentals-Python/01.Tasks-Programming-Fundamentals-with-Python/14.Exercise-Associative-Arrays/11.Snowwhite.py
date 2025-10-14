hat_color_with_names_and_physics = {}

while True:
    try:
        line = input()
    except EOFError:
        break

    if line == "Once upon a time":
        break

    name, hat_color, physics_str = line.split(" <:> ")
    physics = int(physics_str)

    if hat_color not in hat_color_with_names_and_physics:
        hat_color_with_names_and_physics[hat_color] = {}

    # If the dwarf exists, keep the higher physics
    if name in hat_color_with_names_and_physics[hat_color]:
        hat_color_with_names_and_physics[hat_color][name] = max(
            hat_color_with_names_and_physics[hat_color][name], physics
        )
    else:
        hat_color_with_names_and_physics[hat_color][name] = physics

# Flatten into a list of dwarfs with color and physics
final_dwarfs = []
for color, dwarfs in hat_color_with_names_and_physics.items():
    for name, power in dwarfs.items():
        final_dwarfs.append({"name": name, "color": color, "power": power})

# Sort by physics descending
final_dwarfs.sort(key=lambda x: x["power"], reverse=True)

# Sort by number of dwarfs per hat color in case of tie in physics
from collections import Counter

color_counts = Counter()
for dwarf in final_dwarfs:
    color_counts[dwarf["color"]] += 1

final_dwarfs.sort(key=lambda x: (-x["power"], -color_counts[x["color"]]))

for dwarf in final_dwarfs:
    print(f"({dwarf['color']}) {dwarf['name']} <-> {dwarf['power']}")
