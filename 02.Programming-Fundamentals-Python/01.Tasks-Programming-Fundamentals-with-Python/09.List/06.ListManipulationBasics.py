numbers = list(map(int, input().split()))
command = input()

while command != "end":
    parts = command.split()

    if parts[0] == "Add":
        number_to_add = int(parts[1])
        numbers.append(number_to_add)
    elif parts[0] == "Remove":
        remove_number = int(parts[1])
        numbers = [n for n in numbers if n != remove_number]
    elif parts[0] == "RemoveAt":
        remove_at_index = int(parts[1])
        numbers.pop(remove_at_index)
    elif parts[0] == "Insert":
        number = int(parts[1])
        index = int(parts[2])
        numbers.insert(index, number)

    command = input()

print(" ".join(map(str, numbers)))
