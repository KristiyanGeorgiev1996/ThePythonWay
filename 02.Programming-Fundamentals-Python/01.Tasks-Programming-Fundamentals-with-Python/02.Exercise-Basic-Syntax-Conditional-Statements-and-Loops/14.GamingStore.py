current_balance = float(input())
current_balance1 = current_balance

while current_balance1 != 0:
    game = input()
    if game == "Game Time":
        break

    if game in ["OutFall 4", "RoverWatch Origins Edition"]:
        if current_balance1 < 39.99:
            print("Too Expensive")
        else:
            print(f"Bought {game}")
            current_balance1 -= 39.99
    elif game == "CS: OG":
        if current_balance1 < 15.99:
            print("Too Expensive")
        else:
            print(f"Bought {game}")
            current_balance1 -= 15.99
    elif game == "Zplinter Zell":
        if current_balance1 < 19.99:
            print("Too Expensive")
        else:
            print(f"Bought {game}")
            current_balance1 -= 19.99
    elif game == "Honored 2":
        if current_balance1 < 59.99:
            print("Too Expensive")
        else:
            print(f"Bought {game}")
            current_balance1 -= 59.99
    elif game == "RoverWatch":
        if current_balance1 < 29.99:
            print("Too Expensive")
        else:
            print(f"Bought {game}")
            current_balance1 -= 29.99
    else:
        print("Not Found")

    if current_balance1 == 0:
        print("Out of money!")
        break

spent = current_balance - current_balance1
print(f"Total spent: ${spent:.2f}. Remaining: ${current_balance1:.2f}")
