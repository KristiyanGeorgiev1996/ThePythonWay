numbers = list(map(int, input().split()))

while True:
    command = input()
    parts = command.split()

    if command == "end":
        break

    if parts[0] == "Delete":
        number_to_delete = int(parts[1])
        numbers = [n for n in numbers if n != number_to_delete]
    elif parts[0] == "Insert":
        number_to_insert = int(parts[1])
        index_to_insert = int(parts[2])
        numbers.insert(index_to_insert, number_to_insert)

print(" ".join(map(str, numbers)))
