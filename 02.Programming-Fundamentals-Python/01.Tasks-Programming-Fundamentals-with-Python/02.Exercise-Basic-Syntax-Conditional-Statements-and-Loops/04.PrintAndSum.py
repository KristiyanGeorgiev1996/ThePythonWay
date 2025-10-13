number1 = int(input())
number2 = int(input())

all_sum = 0

for i in range(number1, number2 + 1):
    print(i, end=" ")
    all_sum += i

print()
print(f"Sum: {all_sum}")
