x = int(input())

for i in range(1, x + 1):
    line = (str(i) + " ") * (i - 1) + str(i)
    print(line)
