key = int(input())
n = int(input())

for _ in range(n):
    char = input()
    shifted = chr(ord(char) + key)
    print(shifted)
