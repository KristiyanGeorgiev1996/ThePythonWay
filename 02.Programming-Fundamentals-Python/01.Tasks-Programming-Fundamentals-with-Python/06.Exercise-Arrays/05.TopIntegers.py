array = list(map(int, input().split()))

for i in range(len(array)):
    is_top = True
    for j in range(i + 1, len(array)):
        if array[i] <= array[j]:
            is_top = False
            break
    if is_top:
        print(array[i], end=' ' if i != len(array) - 1 else '')
