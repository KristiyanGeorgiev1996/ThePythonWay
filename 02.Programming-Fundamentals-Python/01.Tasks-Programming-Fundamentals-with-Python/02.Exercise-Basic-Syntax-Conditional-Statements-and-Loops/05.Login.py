username = input()
password = username[::-1]
attempts = 4

while attempts > 0:
    attempts -= 1
    typed_pass = input()

    if typed_pass == password:
        print(f"User {username} logged in.")
        break
    else:
        if attempts == 0:
            print(f"User {username} blocked!")
        else:
            print("Incorrect password. Try again.")
