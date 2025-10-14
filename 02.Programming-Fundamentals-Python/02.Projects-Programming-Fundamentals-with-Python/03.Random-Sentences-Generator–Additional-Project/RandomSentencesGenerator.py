import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

def get_random_word(lst):
    return random.choice(lst)

print("Welcome to the Random Sentence Generator!")
print("Press [Enter] to generate a new sentence or type 'exit' to quit.\n")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_adverb = get_random_word(adverbs)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_detail = get_random_word(details)

    sentence = f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}."
    print(sentence)

    user_input = input("Press [Enter] to generate another sentence or type 'exit' to quit: ").strip().lower()
    if user_input == "exit":
        print("Thanks for using the Random Sentence Generator. Goodbye!")
        break
    print()
