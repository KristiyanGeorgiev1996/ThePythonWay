# Store contests and passwords
contests = {}
while True:
    line = input()
    if line == "end of contests":
        break
    contest, password = line.split(":")
    contests[contest] = password

# Store users and their contest points
results = {}
while True:
    line = input()
    if line == "end of submissions":
        break
    contest, password, username, points_str = line.split("=>")
    points = int(points_str)

    if contest in contests and contests[contest] == password:
        if username not in results:
            results[username] = {}
        if contest not in results[username] or results[username][contest] < points:
            results[username][contest] = points

# Determine best candidate
best_user = max(results.items(), key=lambda u: sum(u[1].values()))
best_username = best_user[0]
best_points = sum(best_user[1].values())
print(f"Best candidate is {best_username} with total {best_points} points.")
print("Ranking:")

# Print ranking
for username in sorted(results):
    print(username)
    for contest, points in sorted(results[username].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
