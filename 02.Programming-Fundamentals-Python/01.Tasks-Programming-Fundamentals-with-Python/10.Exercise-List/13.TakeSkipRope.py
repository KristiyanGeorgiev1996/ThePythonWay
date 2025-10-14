word = input()

numbers = []
non_numbers = []

for ch in word:
    if ch.isdigit():
        numbers.append(int(ch))
    else:
        non_numbers.append(ch)

take_list = [numbers[i] for i in range(0, len(numbers), 2)]
skip_list = [numbers[i] for i in range(1, len(numbers), 2)]

result = ""
index_for_skip = 0

for i in range(len(take_list)):
    temp = non_numbers[index_for_skip:index_for_skip + take_list[i]]
    result += "".join(temp)
    index_for_skip += take_list[i] + skip_list[i]

print(result)
