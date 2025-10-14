import re


class Message:
    def __init__(self, planet_name, population, attack_type, soldier_count):
        self.planet_name = planet_name
        self.population = population
        self.attack_type = attack_type
        self.soldier_count = soldier_count


messages_input = [
    "STCDoghudd4=63333$D$0A53333",
    "EHfsytsnhf?8555&I&2C9555SR"
]

messages = []

star_pattern = re.compile(r'[SsTtAaRr]')
msg_pattern = re.compile(
    r'@(?P<planet>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<type>A|D)![^@\-!:>]*->[^@\-!:>]*(?P<soldiers>\d+)'
)

for encrypt_msg in messages_input:
    decryption_key = len(star_pattern.findall(encrypt_msg))

    decrypted_msg = ''.join(chr(ord(ch) - decryption_key) for ch in encrypt_msg)

    match = msg_pattern.search(decrypted_msg)
    if not match:
        continue

    planet = match.group('planet')
    population = int(match.group('population'))
    attack_type = match.group('type')
    soldiers = int(match.group('soldiers'))

    messages.append(Message(planet, population, attack_type, soldiers))

attacked = sorted([m for m in messages if m.attack_type == "A"], key=lambda x: x.planet_name)
destroyed = sorted([m for m in messages if m.attack_type == "D"], key=lambda x: x.planet_name)

print(f"Attacked planets: {len(attacked)}")
for m in attacked:
    print(f"-> {m.planet_name}")

print(f"Destroyed planets: {len(destroyed)}")
for m in destroyed:
    print(f"-> {m.planet_name}")
