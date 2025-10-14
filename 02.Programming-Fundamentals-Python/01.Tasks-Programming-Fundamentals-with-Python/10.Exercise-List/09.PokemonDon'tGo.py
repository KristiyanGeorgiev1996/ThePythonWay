lst = list(map(int, input().split()))
total_sum = 0

while lst:
    index = int(input())

    if index < 0:
        removed = lst[0]
        lst.pop(0)
        lst.insert(0, lst[-1])
    elif index >= len(lst):
        removed = lst[-1]
        lst.pop()
        lst.append(lst[0])
    else:
        removed = lst.pop(index)

    total_sum += removed

    for i in range(len(lst)):
        if lst[i] <= removed:
            lst[i] += removed
        else:
            lst[i] -= removed

print(total_sum)
