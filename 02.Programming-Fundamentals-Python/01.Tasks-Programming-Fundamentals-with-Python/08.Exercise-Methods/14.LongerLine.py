import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

def get_distance_between_two_points(x1, y1, x2, y2):
    side_a = abs(x2 - x1)
    side_b = abs(y2 - y1)
    return math.sqrt(side_a ** 2 + side_b ** 2)

def get_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def point_closer_to_zero(x1, y1, x2, y2):
    return get_hypotenuse(x1, y1) <= get_hypotenuse(x2, y2)

line1 = get_distance_between_two_points(x1, y1, x2, y2)
line2 = get_distance_between_two_points(x3, y3, x4, y4)

line1_point1_is_closer = point_closer_to_zero(x1, y1, x2, y2)
line2_point1_is_closer = point_closer_to_zero(x3, y3, x4, y4)

if line1 >= line2:
    if line1_point1_is_closer:
        print(f"({x1}, {y1})({x2}, {y2})")
    else:
        print(f"({x2}, {y2})({x1}, {y1})")
else:
    if line2_point1_is_closer:
        print(f"({x3}, {y3})({x4}, {y4})")
    else:
        print(f"({x4}, {y4})({x3}, {y3})")
