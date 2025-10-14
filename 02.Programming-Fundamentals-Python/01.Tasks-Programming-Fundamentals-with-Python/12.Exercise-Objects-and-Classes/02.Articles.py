class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

article_data = input().split(', ')
article = Article(article_data[0], article_data[1], article_data[2])

n = int(input())

for _ in range(n):
    command_line = input()
    command_parts = command_line.split(' ')
    action = command_parts[0]
    value = ' '.join(command_parts[1:])

    if action == 'Edit:':
        article.content = value
    elif action == 'ChangeAuthor:':
        article.author = value
    elif action == 'Rename:':
        article.title = value

print(f"{article.title} - {article.content}: {article.author}")
