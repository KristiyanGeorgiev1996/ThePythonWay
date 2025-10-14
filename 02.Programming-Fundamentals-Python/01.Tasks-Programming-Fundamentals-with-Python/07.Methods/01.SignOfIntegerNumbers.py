number = int(input())

def what_is_number(number):
    if number < 0:
        print(f"The number {number} is negative.")
    elif number > 0:
        print(f"The number {number} is positive.")
    else:
        print(f"The number {number} is zero.")

what_is_number(number)
