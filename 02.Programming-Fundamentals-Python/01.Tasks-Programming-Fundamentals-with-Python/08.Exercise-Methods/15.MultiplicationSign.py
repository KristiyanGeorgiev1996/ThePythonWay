num1 = float(input())
num2 = float(input())
num3 = float(input())

def result_sign(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        print("zero")
    elif (
        (n1 > 0 and n2 > 0 and n3 > 0) or
        (n1 < 0 and n2 < 0 and n3 > 0) or
        (n1 < 0 and n2 > 0 and n3 < 0) or
        (n1 > 0 and n2 < 0 and n3 < 0)
    ):
        print("positive")
    else:
        print("negative")

result_sign(num1, num2, num3)
