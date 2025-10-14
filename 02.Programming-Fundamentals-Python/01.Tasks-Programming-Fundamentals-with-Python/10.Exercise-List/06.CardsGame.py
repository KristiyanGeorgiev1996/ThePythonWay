first_hand = list(map(int, input().split()))
second_hand = list(map(int, input().split()))

while first_hand and second_hand:
    first_card = first_hand.pop(0)
    second_card = second_hand.pop(0)

    if first_card > second_card:
        first_hand.extend([first_card, second_card])
    elif second_card > first_card:
        second_hand.extend([second_card, first_card])

if first_hand:
    print(f"First player wins! Sum: {sum(first_hand)}")
else:
    print(f"Second player wins! Sum: {sum(second_hand)}")
