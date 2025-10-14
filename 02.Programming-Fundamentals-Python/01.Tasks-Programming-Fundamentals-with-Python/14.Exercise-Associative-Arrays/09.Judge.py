contests = {}
users = {}

while True:
    line = input()
    if line == "no more time":
        break
    username, contest, points_str = line.split(" -> ")
    points = int(points_str)

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest] or contests[contest][username] < points:
        contests[contest][username] = points

# Print per-contest standings
for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(
        participants.items(),
        key=lambda x: (-x[1], x[0])
    )
    for idx, (name, points) in enumerate(sorted_participants, start=1):
        print(f"{idx}. {name} <::> {points}")

# Aggregate individual total points
for participants in contests.values():
    for username, points in participants.items():
        if username not in users:
            users[username] = points
        else:
            users[username] += points

# Print individual standings
print("Individual standings:")
sorted_users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
for idx, (name, points) in enumerate(sorted_users, start=1):
    print(f"{idx}. {name} -> {points}")
