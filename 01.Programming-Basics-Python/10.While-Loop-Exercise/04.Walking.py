walking_steps = 0

while walking_steps < 10000:
    input_value = input()
    if input_value == "Going home":
        steps_to_home = int(input())
        walking_steps += steps_to_home
        break
    current_steps = int(input_value)
    walking_steps += current_steps

if walking_steps >= 10000:
    steps_over_goal = walking_steps - 10000
    print("Goal reached! Good job!")
    print(f"{steps_over_goal} steps over the goal!")
else:
    steps_to_goal = 10000 - walking_steps
    print(f"{steps_to_goal} more steps to reach goal.")
