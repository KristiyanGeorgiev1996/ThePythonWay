numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()

    if parts[0] == "Add":
        numbers.append(int(parts[1]))
    elif parts[0] == "Insert":
        index = int(parts[2])
        number = int(parts[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            numbers.insert(index, number)
    elif parts[0] == "Remove":
        index = int(parts[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            numbers.pop(index)
    elif parts[0] == "Shift" and parts[1] == "left":
        count = int(parts[2]) % len(numbers)
        for _ in range(count):
            numbers.append(numbers.pop(0))
    elif parts[0] == "Shift" and parts[1] == "right":
        count = int(parts[2]) % len(numbers)
        for _ in range(count):
            numbers.insert(0, numbers.pop())

print(" ".join(map(str, numbers)))
