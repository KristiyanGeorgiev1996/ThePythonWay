math_operation = input()
first_number = float(input())
sec_number = float(input())

def math_operation_func(math_operation):
    result = 0
    if math_operation == "add":
        result = first_number + sec_number
    elif math_operation == "divide":
        result = first_number / sec_number
    elif math_operation == "multiply":
        result = first_number * sec_number
    elif math_operation == "subtract":
        result = first_number - sec_number
    print(result)

math_operation_func(math_operation)
