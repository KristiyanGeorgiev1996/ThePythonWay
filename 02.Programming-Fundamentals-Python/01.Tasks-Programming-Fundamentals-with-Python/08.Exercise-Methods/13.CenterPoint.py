import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def get_first_point(x, y):
    return math.sqrt(abs(x**2) + abs(y**2))

def get_second_point(x, y):
    return math.sqrt(abs(x**2) + abs(y**2))

def get_point_close_to_zero(r1, r2):
    if r1 < r2:
        return -1
    elif r2 < r1:
        return 1
    return 0

result = get_point_close_to_zero(get_first_point(x1, y1), get_second_point(x2, y2))

if result < 0:
    print(f"({x1}, {y1})")
elif result > 0:
    print(f"({x2}, {y2})")
else:
    print(f"({x1}, {y1})")
