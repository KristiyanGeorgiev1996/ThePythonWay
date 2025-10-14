import re

input_text = "Please contact us at support@example.com, admin@my-site.org, or invalid@@mail.com"

pattern = r'[^\.\-_]\b(?![\._\-])[A-Za-z0-9]+[\.\-_]*[A-Za-z0-9]+@[^\.\-](?:[A-Za-z\.\-]+\.)+[A-Za-z]+'

matches = re.findall(pattern, input_text)

for match in matches:
    print(match.strip().strip(','))
