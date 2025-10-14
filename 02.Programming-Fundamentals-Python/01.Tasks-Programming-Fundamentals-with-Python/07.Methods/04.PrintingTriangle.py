n = int(input())

def rectangle(n):
    for i in range(1, n + 1):
        rectangle_row(i)
    for i in range(n - 1, 0, -1):
        rectangle_row(i)

def rectangle_row(n):
    row = " ".join(str(i) for i in range(1, n + 1))
    print(row)

rectangle(n)
