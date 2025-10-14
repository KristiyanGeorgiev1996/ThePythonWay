import re

usernames = input().split(", ")

valid_usernames = [u for u in usernames if re.fullmatch(r"[A-Za-z0-9_-]{3,16}", u)]

for username in valid_usernames:
    print(username)
