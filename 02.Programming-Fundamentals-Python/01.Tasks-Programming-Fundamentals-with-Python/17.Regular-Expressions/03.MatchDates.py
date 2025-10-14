import re

dates_string = "12-Jan-2020, 05/Feb/2021, 23.Mar.2022"
pattern = r'\b(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})\b'

matches = re.finditer(pattern, dates_string)

for match in matches:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")
