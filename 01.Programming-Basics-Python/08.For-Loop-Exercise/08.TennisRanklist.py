tournaments_count = int(input())
initial_points = int(input())

points = 0
wins_count = 0

for _ in range(tournaments_count):
    result = input()
    if result == "W":
        points += 2000
        wins_count += 1
    elif result == "F":
        points += 1200
    elif result == "SF":
        points += 720

average_points = points / tournaments_count
points += initial_points
wins_percent = (wins_count / tournaments_count) * 100

print(f"Final points: {points}")
print(f"Average points: {int(average_points)}")
print(f"{wins_percent:.2f}%")
