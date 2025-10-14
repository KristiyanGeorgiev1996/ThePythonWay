import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

player_score = 0
computer_score = 0
draws = 0

def get_player_move():
    input_move = input("Choose [r]ock, [p]aper or [s]cissors: ").lower()
    if input_move in ("r", "rock"):
        return ROCK
    elif input_move in ("p", "paper"):
        return PAPER
    elif input_move in ("s", "scissors"):
        return SCISSORS
    else:
        print("Invalid input. Please try again...")
        return None

def get_computer_move():
    return random.choice([ROCK, PAPER, SCISSORS])

def determine_winner(player, computer):
    global player_score, computer_score, draws
    if player == computer:
        draws += 1
        return "draw"
    if (player == ROCK and computer == SCISSORS) or \
       (player == PAPER and computer == ROCK) or \
       (player == SCISSORS and computer == PAPER):
        player_score += 1
        return "win"
    computer_score += 1
    return "lose"

def display_result(result):
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    elif result == "draw":
        print("It's a draw!")

def print_score():
    print("==== Score ====")
    print(f"Player:   {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws:    {draws}")
    print("==============\n")

# Game loop
while True:
    print_score()
    player_move = get_player_move()
    if not player_move:
        continue

    computer_move = get_computer_move()
    print(f"Computer chose: {computer_move}")

    result = determine_winner(player_move, computer_move)
    display_result(result)

    answer = input("Do you want to play again? (y/n): ").lower()
    if answer not in ("y", "yes"):
        print("Thanks for playing!")
        break
