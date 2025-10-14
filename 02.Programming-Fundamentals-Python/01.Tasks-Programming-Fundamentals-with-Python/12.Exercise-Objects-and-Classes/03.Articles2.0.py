class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

n = int(input())

for _ in range(n):
    command_array = input().split(', ')
    article = Article(command_array[0], command_array[1], command_array[2])
    print(f"{article.title} - {article.content}: {article.author}")
