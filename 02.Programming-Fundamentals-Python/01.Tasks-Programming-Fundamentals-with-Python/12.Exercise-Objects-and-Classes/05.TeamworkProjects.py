class Team:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.members = []

team_count = int(input())
teams = []

for _ in range(team_count):
    creator, team_name = input().split('-')
    if any(t.name == team_name for t in teams):
        print(f"Team {team_name} was already created!")
    elif any(t.creator == creator for t in teams):
        print(f"{creator} cannot create another team!")
    else:
        new_team = Team(team_name, creator)
        teams.append(new_team)
        print(f"Team {team_name} has been created by {creator}!")

while True:
    command = input()
    if command == 'end of assignment':
        break
    user, team_name = command.split('->')
    team = next((t for t in teams if t.name == team_name), None)
    if not team:
        print(f"Team {team_name} does not exist!")
    elif any(user in t.members or t.creator == user for t in teams):
        print(f"Member {user} cannot join team {team_name}!")
    else:
        team.members.append(user)

valid_teams = sorted(
    [t for t in teams if t.members],
    key=lambda t: (-len(t.members), t.name)
)

for team in valid_teams:
    print(team.name)
    print(f"- {team.creator}")
    for member in sorted(team.members):
        print(f"-- {member}")

disbanded_teams = sorted([t for t in teams if not t.members], key=lambda t: t.name)

print("Teams to disband:")
for team in disbanded_teams:
    print(team.name)
