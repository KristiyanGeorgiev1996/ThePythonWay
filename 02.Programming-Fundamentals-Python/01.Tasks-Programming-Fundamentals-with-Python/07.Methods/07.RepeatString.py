text = input()
count = int(input())

def repeat_string(text, count):
    result = ''
    for _ in range(count):
        result += text
    print(result)

repeat_string(text, count)
