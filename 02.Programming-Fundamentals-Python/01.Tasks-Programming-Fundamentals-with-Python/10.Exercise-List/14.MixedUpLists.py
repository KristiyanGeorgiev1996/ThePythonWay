input_one = list(map(int, input().split()))
input_two = list(map(int, input().split()))

if len(input_one) > len(input_two):
    max_list = input_one[:]
else:
    max_list = input_two[::-1]

rule = sorted([max_list[-2], max_list[-1]])

if len(input_one) > len(input_two):
    input_one = input_one[:-2]
    input_two = input_two[::-1]
else:
    input_two = input_two[:-2]
    input_two = input_two[::-1]

mixed_list = []
for a, b in zip(input_one, input_two):
    mixed_list.extend([a, b])

output = sorted([x for x in mixed_list if rule[0] < x < rule[1]])
print(" ".join(map(str, output)))
