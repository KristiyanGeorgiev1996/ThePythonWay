import re

input_text = "John Doe, jane Smith, Alice Johnson"
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

matches = re.findall(pattern, input_text)

if matches:
    print(" ".join(matches))
