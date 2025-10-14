n = int(input())
vowels = "EeUuIiOoAa"
array_of_sums = []

for _ in range(n):
    name = input()
    sum_vowels = 0
    sum_consonant = 0

    for ch in name:
        if ch in vowels:
            sum_vowels += ord(ch) * len(name)
        else:
            sum_consonant += ord(ch) // len(name)

    array_of_sums.append(sum_vowels + sum_consonant)

array_of_sums.sort()

for val in array_of_sums:
    print(val)
