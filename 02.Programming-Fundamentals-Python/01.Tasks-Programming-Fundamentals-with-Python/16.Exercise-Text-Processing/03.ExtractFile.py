line = input()
file_parts = line.split('\\')
last_part = file_parts[-1]

dot_index = last_part.rfind('.')

name = last_part[:dot_index]
extension = last_part[dot_index + 1:]

print(f"File name: {name}")
print(f"File extension: {extension}")
