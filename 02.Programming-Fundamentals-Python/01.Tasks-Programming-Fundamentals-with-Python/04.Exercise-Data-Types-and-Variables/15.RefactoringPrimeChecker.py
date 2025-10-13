n = int(input())

for i in range(2, n + 1):
    is_prime = True
    for divider in range(2, i):
        if i % divider == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{i} -> true")
    else:
        print(f"{i} -> false")
