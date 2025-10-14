class Player:
    def __init__(self, name):
        self.name = name
        self.positions = {}

    def add_or_update_position(self, position, skill):
        if position not in self.positions or self.positions[position] < skill:
            self.positions[position] = skill

    def total_skill_points(self):
        return sum(self.positions.values())

    def get_positions(self):
        return set(self.positions.keys())


players = {}

while True:
    try:
        command = input()
    except EOFError:
        break

    if command == "Season end":
        break

    if " -> " in command:
        player_name, position, skill_str = command.split(" -> ")
        skill = int(skill_str)
        if player_name not in players:
            players[player_name] = Player(player_name)
        players[player_name].add_or_update_position(position, skill)
    elif " vs " in command:
        first_player, second_player = command.split(" vs ")
        if first_player in players and second_player in players:
            player_one = players[first_player]
            player_two = players[second_player]

            common_positions = player_one.get_positions() & player_two.get_positions()
            if common_positions:
                if player_one.total_skill_points() > player_two.total_skill_points():
                    del players[second_player]
                elif player_two.total_skill_points() > player_one.total_skill_points():
                    del players[first_player]

# Sort players by total skill descending, then name ascending
sorted_players = sorted(
    players.values(),
    key=lambda p: (-p.total_skill_points(), p.name)
)

for player in sorted_players:
    print(f"{player.name}: {player.total_skill_points()} skill")
    # Sort positions by skill descending, then position name ascending
    for position, skill in sorted(player.positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
