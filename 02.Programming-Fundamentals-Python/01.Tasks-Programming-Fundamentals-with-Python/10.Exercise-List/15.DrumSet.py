budget = float(input())

drums = list(map(int, input().split()))
price = drums[:]

while True:
    command = input()
    if command == "Hit it again, Gabsy!":
        break

    hit = int(command)

    for i in range(len(drums)):
        drums[i] -= hit
        if drums[i] <= 0:
            if budget - price[i] * 3 >= 0:
                budget -= price[i] * 3
                drums[i] = price[i]

    for i in range(len(drums) - 1, -1, -1):
        if drums[i] <= 0:
            drums.pop(i)
            price.pop(i)

print(" ".join(map(str, drums)))
print(f"Gabsy has {budget:.2f}lv.")
