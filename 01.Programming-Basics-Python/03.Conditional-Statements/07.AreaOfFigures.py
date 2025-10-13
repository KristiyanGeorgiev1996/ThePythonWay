import math

figure = input()
area = 0

if figure == "square":
    sideA = float(input())
    area = sideA * sideA
elif figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
elif figure == "triangle":
    sideA = float(input())
    heightA = float(input())
    area = sideA * heightA / 2

print(f"{area:.3f}")
