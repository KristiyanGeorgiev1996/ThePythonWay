line = input()
random_strings = line.split()
total_sum = 0

str1 = random_strings[0]
str2 = random_strings[1]
min_len = min(len(str1), len(str2))

for i in range(min_len):
    total_sum += ord(str1[i]) * ord(str2[i])

if len(str1) > len(str2):
    for i in range(min_len, len(str1)):
        total_sum += ord(str1[i])
elif len(str2) > len(str1):
    for i in range(min_len, len(str2)):
        total_sum += ord(str2[i])

print(total_sum)
