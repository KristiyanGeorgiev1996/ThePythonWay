symbols = input().split()

best_count = 0
best_symbol = ""

for i in range(len(symbols) - 1, -1, -1):
    count = 1
    for j in range(i - 1, -1, -1):
        if symbols[i] == symbols[j]:
            count += 1
            if best_count <= count:
                best_count = count
                best_symbol = symbols[i]
        else:
            break

print(' '.join([best_symbol] * best_count))
