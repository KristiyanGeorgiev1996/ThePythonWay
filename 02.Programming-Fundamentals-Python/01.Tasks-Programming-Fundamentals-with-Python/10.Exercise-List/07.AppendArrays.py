numbers = [x for x in input().split("|") if x][::-1]

for group in numbers:
    work = [x for x in group.split(" ") if x]
    for item in work:
        print(item, end=" ")
