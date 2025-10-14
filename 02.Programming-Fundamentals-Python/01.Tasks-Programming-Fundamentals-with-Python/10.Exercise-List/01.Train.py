passengers = list(map(int, input().split()))
max_passengers = int(input())
command = input()

while command != "end":
    parts = command.split()

    if parts[0] == "Add":
        number_to_add = int(parts[1])
        passengers.append(number_to_add)
    else:
        my_int = int(command)
        if my_int <= max_passengers:
            for i in range(len(passengers)):
                if passengers[i] + my_int <= max_passengers:
                    passengers[i] += my_int
                    break

    command = input()

print(" ".join(map(str, passengers)))
