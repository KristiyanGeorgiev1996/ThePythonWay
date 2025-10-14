lines = int(input())
pascal_triangle = []

for row in range(lines):
    pascal_triangle.append([1] * (row + 1))

    for col in range(1, row):
        pascal_triangle[row][col] = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]

for row in pascal_triangle:
    print(" ".join(map(str, row)))
