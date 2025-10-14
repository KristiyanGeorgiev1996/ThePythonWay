n = int(input())
x = int(input())

fact_n = 1
fact_x = 1

for i in range(1, n + 1):
    fact_n *= i
for i in range(1, x + 1):
    fact_x *= i

result = fact_n / fact_x
print(f"{result:.2f}")
