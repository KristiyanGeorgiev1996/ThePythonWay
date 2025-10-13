n = int(input())

for i in range(n):
    first_char = chr(ord('a') + i)
    for j in range(n):
        second_char = chr(ord('a') + j)
        for k in range(n):
            third_char = chr(ord('a') + k)
            print(first_char + second_char + third_char)
