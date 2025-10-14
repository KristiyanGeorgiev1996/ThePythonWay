init_arr = list(map(int, input().split()))

left_fold_index = len(init_arr) // 4 - 1
right_fold_index = 3 * len(init_arr) // 4

top_arr = [0] * (len(init_arr) // 2)
how_many_numbers_so_far = 0

for i in range(left_fold_index, -1, -1):
    top_arr[left_fold_index - i] = init_arr[i]
    how_many_numbers_so_far += 1

for i in range(len(init_arr) - 1, right_fold_index - 1, -1):
    top_arr[len(init_arr) - 1 - i + how_many_numbers_so_far] = init_arr[i]

bottom_arr = [0] * (len(init_arr) // 2)
for i in range(left_fold_index + 1, right_fold_index):
    bottom_arr[i - how_many_numbers_so_far] = init_arr[i]

result = [top_arr[i] + bottom_arr[i] for i in range(len(top_arr))]
print(" ".join(map(str, result)))
