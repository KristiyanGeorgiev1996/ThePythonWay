numbers = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))

result = []
max_length = max(len(numbers), len(numbers2))

for i in range(max_length):
    if i < len(numbers):
        result.append(numbers[i])
    if i < len(numbers2):
        result.append(numbers2[i])

print(" ".join(map(str, result)))
