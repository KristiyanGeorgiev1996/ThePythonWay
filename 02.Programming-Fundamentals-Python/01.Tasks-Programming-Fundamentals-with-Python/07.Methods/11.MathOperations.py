first_number = float(input())
calculation = input()
second_number = float(input())

sum_result = 0

def math_operations(first_number, second_number):
    global sum_result
    if calculation == "*":
        sum_result = first_number * second_number
    elif calculation == "+":
        sum_result = first_number + second_number
    elif calculation == "/":
        sum_result = first_number / second_number
    elif calculation == "-":
        sum_result = first_number - second_number

math_operations(first_number, second_number)
print(sum_result)
