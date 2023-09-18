import json

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


def read_in_games_data(teams):
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

    return teams