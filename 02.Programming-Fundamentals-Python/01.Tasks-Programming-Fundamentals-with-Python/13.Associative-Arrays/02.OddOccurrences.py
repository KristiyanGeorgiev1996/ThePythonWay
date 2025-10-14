words = input().split()
counts = {}

for word in words:
    lower = word.lower()
    counts[lower] = counts.get(lower, 0) + 1

for word, count in counts.items():
    if count % 2 == 1:
        print(word, end=' ')
