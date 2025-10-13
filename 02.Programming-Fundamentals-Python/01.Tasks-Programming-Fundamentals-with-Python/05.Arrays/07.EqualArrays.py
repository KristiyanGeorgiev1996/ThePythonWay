array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

sum_of_all_numbers = 0
identical = True

for i in range(len(array1)):
    if array1[i] != array2[i]:
        print(f"Arrays are not identical. Found difference at {i} index")
        identical = False
        break
    else:
        sum_of_all_numbers += array1[i]

if identical:
    print(f"Arrays are identical. Sum: {sum_of_all_numbers}")
