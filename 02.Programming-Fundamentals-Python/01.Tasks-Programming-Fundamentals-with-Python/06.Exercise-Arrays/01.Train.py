n = int(input())
array = []
total_sum = 0

for _ in range(n):
    number = int(input())
    array.append(number)
    total_sum += number

print(' '.join(map(str, array)))
print(total_sum)
