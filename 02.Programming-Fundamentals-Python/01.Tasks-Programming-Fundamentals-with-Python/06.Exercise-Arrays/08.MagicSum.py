array = list(map(int, input().split()))
number = int(input())

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] + array[j] == number:
            print(f"{array[i]} {array[j]}")
