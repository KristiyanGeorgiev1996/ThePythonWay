position_in_fibonacci_sequence = int(input())
fibonacci_sequence = [0] * 50

fibonacci_sequence[0] = 1
fibonacci_sequence[1] = 1

if position_in_fibonacci_sequence > 2:
    for i in range(2, position_in_fibonacci_sequence):
        fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]

print(fibonacci_sequence[position_in_fibonacci_sequence - 1])
