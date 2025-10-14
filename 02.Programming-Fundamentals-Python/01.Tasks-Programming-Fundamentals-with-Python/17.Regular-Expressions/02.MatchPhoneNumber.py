import re

phones = "+359 2 222 2222, +359-2-333-3333, 12345"
pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'

matches = re.findall(pattern, phones)  # This returns only the captured group, so we need a trick

# To get the full match, use re.finditer
matches = [m.group(0) for m in re.finditer(pattern, phones)]

if matches:
    print(", ".join(matches))
