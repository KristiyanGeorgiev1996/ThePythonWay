width = int(input())
length = int(input())

cake_pieces = width * length

while True:
    input_value = input()
    if input_value == "STOP":
        break
    current_pieces = int(input_value)
    cake_pieces -= current_pieces
    if cake_pieces < 0:
        break

if cake_pieces >= 0:
    print(f"{cake_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
