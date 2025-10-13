numbers_count = int(input())

p1 = p2 = p3 = p4 = p5 = 0

for _ in range(numbers_count):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    else:
        p5 += 1

print(f"{(p1 / numbers_count * 100):.2f}%")
print(f"{(p2 / numbers_count * 100):.2f}%")
print(f"{(p3 / numbers_count * 100):.2f}%")
print(f"{(p4 / numbers_count * 100):.2f}%")
print(f"{(p5 / numbers_count * 100):.2f}%")
