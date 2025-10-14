n = float(input())
x = float(input())

def math_power(n, x):
    if n != 0 and x != 0:
        result = n ** x
        print(result)
    else:
        print(0)

math_power(n, x)
