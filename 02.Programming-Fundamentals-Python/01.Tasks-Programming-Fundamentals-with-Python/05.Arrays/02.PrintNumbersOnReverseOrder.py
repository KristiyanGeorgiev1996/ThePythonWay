numbers = int(input())
array = []

for _ in range(numbers):
    array.append(int(input()))

for num in reversed(array):
    print(num, end=" ")
