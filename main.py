import json
from pprint import pprint

# open and read file
with open('2022_games_data.json') as file:
    games_data = json.load(file)

# pprint(games_data[0])

# team_scores = {'team_name': [scores] }
team_scores = {}

# look at each game in file and store home team/points, away team/points
for game in games_data:

    home_team_name = game['home_team']
    home_team_points = game['home_points']

    away_team_name = game['away_team']
    away_team_points = game['away_points']

    # store home data
    if home_team_name not in team_scores:
        team_scores[home_team_name] = []

    if home_team_points is not None:
        team_scores[home_team_name].append(home_team_points)

    # same for away team
    if away_team_name not in team_scores:
        team_scores[away_team_name] = []

    if away_team_points is not None:
        team_scores[away_team_name].append(away_team_points)



# pprint(team_scores)

# team_ppg = { 'team_name': ppg }
team_ppg = {}

# look at each team and calculate average points per game (ppg)
for team_name, scores in team_scores.items():
    if len(scores) > 0:
        team_ppg[team_name] = round(sum(scores)/len(scores), 2)

# pprint(team_ppg)

# order the teams by most to least ppg
sorted_team_ppg = sorted(team_ppg.items(), key=lambda item: item[1], reverse=True)

pprint(sorted_team_ppg)

# output a pretty table
print("Rank\t| PPG\t| Team name")
print("-----------------------------------")
i = 0
last_ppg = 9999999
for (team_name, ppg) in sorted_team_ppg:
    if last_ppg != ppg:
        i = i + 1
    
    print(str(i) + "\t| " + str(ppg) + "\t| " + team_name)

    last_ppg = ppg
