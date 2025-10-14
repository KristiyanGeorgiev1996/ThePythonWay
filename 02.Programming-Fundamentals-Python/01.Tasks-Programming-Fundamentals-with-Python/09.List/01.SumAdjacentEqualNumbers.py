numbers = list(map(int, input().split()))

i = 0
while i < len(numbers) - 1:
    if numbers[i] == numbers[i + 1]:
        numbers[i] += numbers[i + 1]
        numbers.pop(i + 1)
        i = 0
    else:
        i += 1

print(" ".join(map(str, numbers)))
