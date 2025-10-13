favorite_book = input()
is_found = False
book_counter = 0

input_value = input()
while input_value != "No More Books":
    if input_value == favorite_book:
        is_found = True
        break
    book_counter += 1
    input_value = input()

if is_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
