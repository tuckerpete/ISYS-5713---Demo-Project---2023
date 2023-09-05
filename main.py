import json
from pprint import pprint

# The Team class hold information about team objects
class Team:
    # This method gets called when a new Team is created. Data from the data file will be passed to this method
    def __init__(self, data):
        self.id = data['id']
        self.school = data['school']
        self.mascot = data['mascot']
        self.abbreviation = data['abbreviation']
        self.conference = data['conference']
        self.color = data['color']
        self.alt_color = data['alt_color']
        self.logo = None
        if data['logos'] is not None:
            self.logo = data['logos'][0]
        self.games = []
        self.ppg = 0

    # This method adds a Game object to the "games" list of this Team object and then calculates the team's PPG
    def add_game(self, game):
        self.games.append(game)
        self.calculate_ppg()

    # This method calculates the team's average points-per-game (ppg)
    def calculate_ppg(self):
        scores = []
        for game in self.games:
            points = game.scores[self.id]
            if points is not None:
                scores.append(points)
        if len(scores) > 0:
            self.ppg = round(sum(scores)/len(scores), 2)

    # This method gets called whenever we try to print a Team object
    def __str__(self):
        return f"Team(id='{self.id}', school='{self.school}', conference='{self.conference}')"


# The Game class hold information about game objects
class Game:
    # This method gets called when a new Game is created. Data from the data file will be passed to this method
    def __init__(self, data):
        self.id = data['id']
        self.season = data['season']
        self.week = data['week']
        self.date = data['start_date']
        self.venue = data['venue']
        self.home_team_name = data['home_team']
        self.away_team_name = data['away_team']
        self.scores = {data['home_id']: data['home_points'],
                       data['away_id']: data['away_points']}
        
    # This method gets called whenever we try to print a Game object
    def __str__(self):
        return f"Game(id='{self.id}', season='{self.season}', week='{self.week}', matchup='{self.away_team_name} vs. {self.home_team_name}')"


# open and read teams data file
with open('teams_data.json') as file:
    teams_data = json.load(file)

# teams = {'team_id': Team object}   <-- This will hold our Teams objects
teams = {}

# loop through the teams in the data file and create Team objects
for team_data in teams_data:
    teams[team_data['id']] = Team(team_data)

# open and read games data file
with open('2022_games_data.json') as file:
    games_data = json.load(file)

# loop through the games in the data file and create Game objects 
for game_data in games_data:
    game = Game(game_data)
    # Add this game object to the "games" list in both the home and away team objects 
    teams[game_data['home_id']].add_game(game)
    teams[game_data['away_id']].add_game(game)
    # print(game)

# order the teams by most to least ppg
teams_sorted_by_ppg = sorted(teams.values(), key=lambda team: team.ppg, reverse=True)

# output a pretty table
print("Rank\t| PPG\t| Team name")
print("-----------------------------------")
i = 0
last_ppg = 9999999
for team_object in teams_sorted_by_ppg:
    ppg = team_object.ppg
    if ppg == 0:
        break
    if last_ppg != ppg:
        i = i + 1
    
    print(str(i) + "\t| " + str(ppg) + "\t| " + team_object.school)

    last_ppg = ppg
