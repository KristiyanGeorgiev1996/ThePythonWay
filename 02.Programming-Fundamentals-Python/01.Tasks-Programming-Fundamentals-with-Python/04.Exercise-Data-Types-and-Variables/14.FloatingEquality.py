eps = 0.000001

n1 = float(input())
n2 = float(input())

is_equal = abs(n1 - n2) < eps

if is_equal:
    print("True")
else:
    print("False")
