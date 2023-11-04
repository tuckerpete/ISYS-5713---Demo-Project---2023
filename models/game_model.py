import json
import requests
from models import base_model
from models.score_model import Score

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

# The Game class hold information about game objects
class Game(base_model.Base):
    __tablename__ = "game"

    id: Mapped[int] = mapped_column(primary_key=True)
    season: Mapped[int]
    week: Mapped[int]
    date: Mapped[str]
    venue: Mapped[Optional[str]]
    
    scores: Mapped[List["Score"]] = relationship(back_populates="game")

    def __repr__(self):
        return f"Game(id='{self.id}', season='{self.season}', week='{self.week}', matchup='{self.away_team_name} vs. {self.home_team_name}')"


def read_in_games_data():
    
    # read games data from API
    base_url = 'https://api.collegefootballdata.com'
    endpoint = '/games?year=2023'

    with open('auth_key.txt', 'r') as auth_file:
        auth_key = auth_file.read()

    header = {'Authorization': f'Bearer {auth_key}'}

    response = requests.get(base_url + endpoint, headers=header)

    if response.status_code == 200:
        games_data = response.json()
    else:
        print(f'ERROR Code {response.status_code} - {response.reason} - {response.text}')
        exit()

    # open a session with the database
    with Session(base_model.engine) as session:

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
                
                session.add(Score(game_id=game_data['id'],
                                  team_id=game_data['home_id'],
                                  team_side='Home',
                                  points=game_data['home_points']))
                
                session.add(Score(game_id=game_data['id'],
                                  team_id=game_data['away_id'],
                                  team_side='Away',
                                  points=game_data['away_points']))

        session.commit()


def get_seasons_list():
    with Session(base_model.engine) as session:
        season_results = session.query(Game.season).distinct().order_by(Game.season).all()
    return [season[0] for season in season_results]