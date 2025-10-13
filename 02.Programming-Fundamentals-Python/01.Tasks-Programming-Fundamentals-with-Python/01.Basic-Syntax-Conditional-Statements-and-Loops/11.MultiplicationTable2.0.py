first_num = int(input())
second_num = int(input())

if second_num <= 10:
    for times in range(second_num, 11):
        product = first_num * times
        print(f"{first_num} X {times} = {product}")
else:
    product = first_num * second_num
    print(f"{first_num} X {second_num} = {product}")
