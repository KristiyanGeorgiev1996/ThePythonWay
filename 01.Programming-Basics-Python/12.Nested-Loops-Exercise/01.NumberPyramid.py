n = int(input())

current_number = 0
is_bigger = False

for row in range(1, n + 1):
    line = ""
    for col in range(1, row + 1):
        current_number += 1
        if current_number > n:
            is_bigger = True
            break
        line += str(current_number) + " "
    print(line.strip())
    if is_bigger:
        break
