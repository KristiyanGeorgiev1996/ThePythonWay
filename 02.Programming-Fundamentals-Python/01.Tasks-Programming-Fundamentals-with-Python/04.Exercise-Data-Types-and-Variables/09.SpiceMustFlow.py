dobivs = float(input())

days = 0
all_dobiv = 0

while True:
    if dobivs >= 100:
        days += 1
        n = dobivs - 26
        all_dobiv += n
        dobivs -= 10
    else:
        all_dobiv -= 26
        if all_dobiv < 0:
            all_dobiv = 0
        dobivs -= 10
        break

    if dobivs < 0:
        break

print(days)
print(all_dobiv)
