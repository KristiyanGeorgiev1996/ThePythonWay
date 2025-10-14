n = int(input())
parking_card = {}

for _ in range(n):
    parts = input().split()
    action = parts[0]
    username = parts[1]

    if action == "register":
        plate_number = parts[2]
        if username not in parking_card:
            parking_card[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_card[username]}")
    elif action == "unregister":
        if username not in parking_card:
            print(f"ERROR: user {username} not found")
        else:
            del parking_card[username]
            print(f"{username} unregistered successfully")

for user, plate in parking_card.items():
    print(f"{user} => {plate}")
