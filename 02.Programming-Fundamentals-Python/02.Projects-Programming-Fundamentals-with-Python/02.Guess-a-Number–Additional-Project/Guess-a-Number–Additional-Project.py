import random
import os

play_again = True
level = 1
min_num = 1
max_num = 100

while play_again:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Welcome to Guess the Number - Level {level} ({min_num} - {max_num})")

    secret_number = random.randint(min_num, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Enter your guess ({min_num} - {max_num}): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < min_num or guess > max_num:
            print("Number out of range.")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

    answer = input("Do you want to play again? (y/n): ").lower()
    if answer not in ("y", "yes"):
        print("Thanks for playing!")
        play_again = False
    else:
        level += 1
        max_num += 100
