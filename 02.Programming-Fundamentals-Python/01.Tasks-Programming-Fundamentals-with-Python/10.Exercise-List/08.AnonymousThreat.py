lst = input().split(' ')

while True:
    line = input()
    if line == "3:1":
        break

    data = line.split(' ')
    start = int(data[1])
    end = int(data[2])

    if data[0] == "merge":
        if start < 0:
            start = 0
        if end >= len(lst):
            end = len(lst) - 1

        for _ in range(end - start):
            lst[start] += lst[start + 1]
            lst.pop(start + 1)

    if data[0] == "divide":
        part_size = len(lst[start]) // end
        counter = end
        off = 1

        while counter > 1:
            counter -= 1
            lst.insert(start + off, lst[start][:part_size])
            off += 1
            lst[start] = lst[start][part_size:]

        lst.insert(start + off, lst[start])
        lst.pop(start)

print(' '.join(lst))
