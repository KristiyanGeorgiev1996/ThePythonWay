numbers = list(map(int, input().split()))
result = []

for num in numbers:
    if num > 0:
        result.append(num)

result.reverse()

if len(result) == 0:
    print("empty")
else:
    print(" ".join(map(str, result)))
