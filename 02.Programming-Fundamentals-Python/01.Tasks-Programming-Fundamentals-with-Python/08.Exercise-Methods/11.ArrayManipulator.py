numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    parts = command.split()
    main_command = parts[0]

    if main_command == "exchange":
        index = int(parts[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            numbers = numbers[index + 1:] + numbers[:index + 1]

    elif main_command in ("max", "min"):
        type_ = parts[1]
        filtered = [num for num in numbers if (num % 2 == 0 if type_ == "even" else num % 2 != 0)]
        if not filtered:
            print("No matches")
        else:
            if main_command == "max":
                target = max(filtered)
            else:
                target = min(filtered)
            # get last occurrence of target
            idx = len(numbers) - 1 - numbers[::-1].index(target)
            print(idx)

    elif main_command in ("first", "last"):
        count = int(parts[1])
        type_ = parts[2]
        if count > len(numbers):
            print("Invalid count")
        else:
            filtered = [num for num in numbers if (num % 2 == 0 if type_ == "even" else num % 2 != 0)]
            if main_command == "first":
                result = filtered[:count]
            else:
                result = filtered[-count:]
            print(result)

print(numbers)
