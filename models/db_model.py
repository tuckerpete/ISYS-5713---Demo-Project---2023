from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import func

import json

# Defining these here so that they can be used throughout the whole file
engine = None
Team = None
Game = None
Score = None


def create_database():

    # create the engine
    global engine
    engine = create_engine("sqlite:///models/cache.sqlite")

    # SQLAlchemy is smart enough to read the classes from our existing database
    # For more information on Automapping, see here: https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    # Now that we've automapped the classes, we can save them to some global variables
    global Team, Game, Score
    Team = Base.classes.team
    Game = Base.classes.game
    Score = Base.classes.score


def read_in_teams_data():
    # open and read teams data file
    with open('models/teams_data.json') as file:
        teams_data = json.load(file)

    # open a session with the database
    with Session(engine) as session:

        # find what teams are already in the database
        existing_teams = session.query(Team).all()
        existing_team_ids = []
        for team in existing_teams:
            existing_team_ids.append(team.id)

        # loop through team data from the file
        for team_data in teams_data:

            if team_data['id'] not in existing_team_ids:
                session.add(Team(id=team_data['id'],
                                school=team_data['school'],
                                mascot=team_data['mascot'],
                                abbreviation=team_data['abbreviation'],
                                conference=team_data['conference'],
                                color=team_data['color'],
                                alt_color=team_data['alt_color']))

        session.commit()


def rank_teams_by_ppg():
    # order the teams by most to least ppg
    # teams_sorted_by_ppg = sorted(teams.values(), key=lambda team: team.ppg, reverse=True)
    with Session(engine) as session:
        teams_sorted_by_ppg = session.query(Team.school, func.avg(Score.points)).join(Score).group_by(Team.id).order_by(func.avg(Score.points).desc()).all()
    return teams_sorted_by_ppg


def read_in_games_data():
    # open and read games data file
    with open('models/2022_games_data.json') as file:
        games_data = json.load(file)

    # open a session with the database
    with Session(engine) as session:

        # find what teams are already in the database
        existing_games = session.query(Game).all()
        existing_game_ids = []
        for game in existing_games:
            existing_game_ids.append(game.id)

        # loop through team data from the file
        for game_data in games_data:

            if game_data['id'] not in existing_game_ids:
                session.add(Game(id=game_data['id'],
                                 season=game_data['season'],
                                 week=game_data['week'],
                                 date=game_data['start_date'],
                                 venue=game_data['venue']))
                
                session.add(Score(team_id=game_data['home_id'],
                                  game_id=game_data['id'],
                                  team_side='Home',
                                  points=game_data['home_points']))
                
                session.add(Score(team_id=game_data['away_id'],
                                  game_id=game_data['id'],
                                  team_side='Away',
                                  points=game_data['away_points']))

        session.commit()