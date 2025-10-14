import random

phrases = [
    "Excellent product.", "Such a great product.", "I always use that product.",
    "Best product of its category.", "Exceptional product.", "I can't live without this product."
]

events = [
    "Now I feel good.", "I have succeeded with this product.", "Makes miracles. I am happy of the results!",
    "I cannot believe but now I feel awesome.", "Try it yourself, I am very satisfied.", "I feel great!"
]

authors = ["Diana", "Petya", "Stella", "Elena", "Katya", "Iva", "Annie", "Eva"]

cities = ["Burgas", "Sofia", "Plovdiv", "Varna", "Ruse"]

number_of_messages = int(input("Enter the number of messages to generate: "))

for _ in range(number_of_messages):
    phrase = random.choice(phrases)
    event_text = random.choice(events)
    author = random.choice(authors)
    city = random.choice(cities)
    print(f"{phrase} {event_text} {author} – {city}.")
