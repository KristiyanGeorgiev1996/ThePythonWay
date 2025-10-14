num_list = list(map(int, input().split()))
bomb_arr = list(map(int, input().split()))

item_to_kill = bomb_arr[0]
range_to_kill = bomb_arr[1]

while item_to_kill in num_list:
    index = num_list.index(item_to_kill)

    left_range = range_to_kill
    right_range = range_to_kill

    if index - left_range < 0:
        left_range = index
    if index + right_range >= len(num_list):
        right_range = len(num_list) - index - 1

    del num_list[index - left_range : index + right_range + 1]

print(sum(num_list))
