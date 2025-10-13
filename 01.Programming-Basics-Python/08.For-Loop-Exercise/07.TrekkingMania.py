groups_count = int(input())

people_count = 0
people_musala = 0
people_monblan = 0
people_kilimandzharo = 0
people_k2 = 0
people_everest = 0

for _ in range(groups_count):
    current_people = int(input())
    people_count += current_people

    if current_people <= 5:
        people_musala += current_people
    elif 6 <= current_people <= 12:
        people_monblan += current_people
    elif 13 <= current_people <= 25:
        people_kilimandzharo += current_people
    elif 26 <= current_people <= 40:
        people_k2 += current_people
    else:
        people_everest += current_people

print(f"{(people_musala / people_count * 100):.2f}%")
print(f"{(people_monblan / people_count * 100):.2f}%")
print(f"{(people_kilimandzharo / people_count * 100):.2f}%")
print(f"{(people_k2 / people_count * 100):.2f}%")
print(f"{(people_everest / people_count * 100):.2f}%")
