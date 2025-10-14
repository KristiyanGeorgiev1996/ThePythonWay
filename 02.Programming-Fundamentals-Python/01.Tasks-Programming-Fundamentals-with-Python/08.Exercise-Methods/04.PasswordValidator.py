password = input()

def password_valid(password):
    length = 6 <= len(password) <= 10
    letters_digits = True
    counter_digits = 0

    for char in password:
        if char.isdigit():
            counter_digits += 1
        if not char.isalnum():
            letters_digits = False

    if not length:
        print("Password must be between 6 and 10 characters")
    if not letters_digits:
        print("Password must consist only of letters and digits")
    if counter_digits < 2:
        print("Password must have at least 2 digits")

    if length and letters_digits and counter_digits >= 2:
        print("Password is valid")

password_valid(password)
