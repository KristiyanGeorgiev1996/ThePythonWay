a = float(input())
b = float(input())
operation = input()

result = 0
isEven = False

if operation == '+':
    result = a + b
    isEven = result % 2 == 0
    if isEven:
        print(f"{a} + {b} = {result} - even")
    else:
        print(f"{a} + {b} = {result} - odd")
elif operation == '-':
    result = a - b
    isEven = result % 2 == 0
    if isEven:
        print(f"{a} - {b} = {result} - even")
    else:
        print(f"{a} - {b} = {result} - odd")
elif operation == '*':
    result = a * b
    isEven = result % 2 == 0
    if isEven:
        print(f"{a} * {b} = {result} - even")
    else:
        print(f"{a} * {b} = {result} - odd")
elif operation == '/':
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        result = a / b
        print(f"{a} / {b} = {result:.2f}")
elif operation == '%':
    if b == 0:
        print(f"Cannot divide {a} by zero")
    else:
        result = a % b
        print(f"{a} % {b} = {result}")
