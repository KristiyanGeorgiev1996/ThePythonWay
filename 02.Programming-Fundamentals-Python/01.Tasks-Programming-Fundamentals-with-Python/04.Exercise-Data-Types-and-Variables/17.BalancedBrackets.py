n = int(input())
open_count = 0
close_count = 0
balanced = True

for _ in range(n):
    char = input()
    if char == "(":
        open_count += 1
    elif char == ")":
        close_count += 1
        if open_count - close_count != 0:
            balanced = False
            break

if open_count == close_count and balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
