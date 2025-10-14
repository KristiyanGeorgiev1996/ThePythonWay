n = int(input())
word_synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in word_synonyms:
        word_synonyms[word] = []
    word_synonyms[word].append(synonym)

for word, synonyms in word_synonyms.items():
    print(f"{word} - {', '.join(synonyms)}")
