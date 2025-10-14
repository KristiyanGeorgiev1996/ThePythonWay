numbers_of_read = int(input())

arr1 = [0] * numbers_of_read
arr2 = [0] * numbers_of_read

for i in range(numbers_of_read):
    numbers = list(map(int, input().split()))

    if i % 2 == 0:
        arr1[i] = numbers[0]
        arr2[i] = numbers[1]
    else:
        arr1[i] = numbers[1]
        arr2[i] = numbers[0]

print(' '.join(map(str, arr1)))
print(' '.join(map(str, arr2)))
