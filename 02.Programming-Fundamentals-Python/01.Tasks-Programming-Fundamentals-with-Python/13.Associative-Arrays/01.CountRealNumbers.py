numbers = list(map(int, input().split()))
counts = {}

for num in numbers:
    counts[num] = counts.get(num, 0) + 1

for num in sorted(counts.keys()):
    print(f"{num} -> {counts[num]}")
