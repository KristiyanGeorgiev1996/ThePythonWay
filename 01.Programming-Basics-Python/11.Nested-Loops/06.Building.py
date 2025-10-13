count_of_floors = int(input())
count_of_rooms = int(input())

for floor in range(count_of_floors, 0, -1):
    line = ""
    for room in range(count_of_rooms):
        if floor == count_of_floors:
            line += f"L{floor}{room} "
        elif floor % 2 == 0:
            line += f"O{floor}{room} "
        else:
            line += f"A{floor}{room} "
    print(line.strip())
