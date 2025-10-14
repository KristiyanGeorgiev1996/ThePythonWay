first = float(input())
second = float(input())
third = float(input())

def what_is_low(first, second, third):
    if first <= second and first <= third:
        print(first)
    elif second <= first and second <= third:
        print(second)
    else:
        print(third)

what_is_low(first, second, third)
