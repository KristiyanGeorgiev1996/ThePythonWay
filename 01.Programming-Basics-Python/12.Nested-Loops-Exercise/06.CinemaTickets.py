student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    seats_count = int(input())
    sold_tickets = 0

    while True:
        ticket_type = input()
        if ticket_type == "End":
            break

        sold_tickets += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if sold_tickets == seats_count:
            break

    total_tickets += sold_tickets
    print(f"{movie_name} - {(sold_tickets / seats_count * 100):.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets * 100):.2f}% kids tickets.")
