sequence = list(map(int, input().split()))

lengths = [1] * len(sequence)
previous = [-1] * len(sequence)
max_length = 0
last_index = -1

for i in range(len(sequence)):
    for j in range(i):
        if sequence[j] < sequence[i] and lengths[j] >= lengths[i]:
            lengths[i] = lengths[j] + 1
            previous[i] = j
    if lengths[i] > max_length:
        max_length = lengths[i]
        last_index = i

lis = []
while last_index != -1:
    lis.append(sequence[last_index])
    last_index = previous[last_index]

lis.reverse()
print(" ".join(map(str, lis)))
