n = int(input())
names = []

for _ in range(n):
    name_going = input().split()

    if name_going[-2] == "is":
        if name_going[0] not in names:
            names.append(name_going[0])
        else:
            print(f"{name_going[0]} is already in the list!")
    elif name_going[-2] == "not":
        if name_going[0] in names:
            names.remove(name_going[0])
        else:
            print(f"{name_going[0]} is not in the list!")

for name in names:
    print(name)
