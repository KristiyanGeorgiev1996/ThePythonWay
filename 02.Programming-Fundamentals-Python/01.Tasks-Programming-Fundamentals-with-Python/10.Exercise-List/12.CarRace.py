nums = list(map(int, input().split()))

time_l = 0
time_r = 0
mid = len(nums) // 2

for i in range(mid):
    time_l += nums[i]
    if nums[i] == 0:
        time_l *= 0.8

for i in range(len(nums) - 1, mid, -1):
    time_r += nums[i]
    if nums[i] == 0:
        time_r *= 0.8

if time_l < time_r:
    print(f"The winner is left with total time: {time_l}")
else:
    print(f"The winner is right with total time: {time_r}")
