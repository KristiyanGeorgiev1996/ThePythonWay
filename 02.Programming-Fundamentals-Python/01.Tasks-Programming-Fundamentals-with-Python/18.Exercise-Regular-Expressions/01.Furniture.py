import re

class Furniture:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity

furnitures = []
pattern = re.compile(r'>>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)')

input_lines = [
    ">>Chair<<412.23!3",
    ">>Sofa<<500!5",
    ">>Recliner<<<<!5",
    ">>Bench<<230!10",
    ">>>>>>Rocking chair<<!5",
    ">>Bed<<700!5",
    "Purchase"
]

for line in input_lines:
    if line == "Purchase":
        break
    match = pattern.search(line)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(4))
        furnitures.append(Furniture(name, price, quantity))

print("Bought furniture:")
total_spend = 0
for f in furnitures:
    print(f.name)
    total_spend += f.total

print(f"Total money spend: {total_spend:.2f}")
