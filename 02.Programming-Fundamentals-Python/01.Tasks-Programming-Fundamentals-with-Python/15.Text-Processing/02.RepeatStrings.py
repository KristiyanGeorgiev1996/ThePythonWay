line = input()
words = line.split(" ")

for word in words:
    for _ in range(len(word)):
        print(word, end='')  # print without newline

print()  # move to a new line at the end
