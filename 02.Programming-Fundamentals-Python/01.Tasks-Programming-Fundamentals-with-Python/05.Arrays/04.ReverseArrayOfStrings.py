array = input().split()

for i in range(len(array) // 2):
    array[i], array[-1 - i] = array[-1 - i], array[i]

print(" ".join(array))
