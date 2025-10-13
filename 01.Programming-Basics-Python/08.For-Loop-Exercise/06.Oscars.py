actor_name = input()
academy_points = float(input())
jury_count = int(input())

points = academy_points

for _ in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    points += len(jury_name) * jury_points / 2

    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break

if points <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - points:.1f} more!")
