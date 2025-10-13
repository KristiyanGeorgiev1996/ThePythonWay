odd = int(input())
sum_ = 0

for i in range(1, odd * 2, 2):
    sum_ += i
    print(i)

print(f"Sum: {sum_}")
