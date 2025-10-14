numbers = list(map(int, input().split()))
result = []

for i in range(len(numbers) // 2):
    current_result = numbers[i] + numbers[-1 - i]
    result.append(current_result)

if len(numbers) % 2 == 1:
    result.append(numbers[len(numbers) // 2])

print(" ".join(map(str, result)))
