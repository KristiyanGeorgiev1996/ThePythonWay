n = int(input())
fruits = []

for _ in range(n):
    fruits.append(input())

fruits.sort()

for i in range(len(fruits)):
    print(f"{i + 1}.{fruits[i]}")
