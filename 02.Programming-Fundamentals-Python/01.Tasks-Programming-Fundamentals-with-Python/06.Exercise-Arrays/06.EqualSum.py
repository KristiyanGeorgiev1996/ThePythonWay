values = list(map(int, input().split()))
is_found = False

for i in range(len(values)):
    left_sum = sum(values[:i])
    right_sum = sum(values[i+1:])

    if left_sum == right_sum and not is_found:
        print(i)
        is_found = True

if not is_found:
    print("no")
