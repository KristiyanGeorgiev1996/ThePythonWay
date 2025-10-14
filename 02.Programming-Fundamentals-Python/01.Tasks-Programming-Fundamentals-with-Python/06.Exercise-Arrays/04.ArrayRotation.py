numbers = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    first_num = numbers.pop(0)
    numbers.append(first_num)

print(' '.join(map(str, numbers)))
