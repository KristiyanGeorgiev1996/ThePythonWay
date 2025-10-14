numbers = list(map(int, input().split()))
change = False

while True:
    command = input()
    if command == "end":
        break

    tokens = command.split()
    if tokens[0] == "Add":
        numbers.append(int(tokens[1]))
        change = True
    elif tokens[0] == "Remove":
        remove_number = int(tokens[1])
        numbers = [n for n in numbers if n != remove_number]
        change = True
    elif tokens[0] == "RemoveAt":
        numbers.pop(int(tokens[1]))
        change = True
    elif tokens[0] == "Insert":
        numbers.insert(int(tokens[2]), int(tokens[1]))
        change = True
    elif tokens[0] == "Contains":
        print("Yes" if int(tokens[1]) in numbers else "No such number")
    elif tokens[0] == "PrintEven":
        print(" ".join(map(str, [n for n in numbers if n % 2 == 0])))
    elif tokens[0] == "PrintOdd":
        print(" ".join(map(str, [n for n in numbers if n % 2 != 0])))
    elif tokens[0] == "GetSum":
        print(sum(numbers))
    elif tokens[0] == "Filter":
        sign = tokens[1]
        number_f = int(tokens[2])
        if sign == ">":
            filtered = [n for n in numbers if n > number_f]
        elif sign == "<":
            filtered = [n for n in numbers if n < number_f]
        elif sign == ">=":
            filtered = [n for n in numbers if n >= number_f]
        elif sign == "<=":
            filtered = [n for n in numbers if n <= number_f]
        print(" ".join(map(str, filtered)))

if change:
    print(" ".join(map(str, numbers)))
