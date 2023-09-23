import json
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

### OLD Game Class
# class Game:
#     # This method gets called when a new Game is created. Data from the data file will be passed to this method
#     def __init__(self, data):
#         self.id = data['id']
#         self.season = data['season']
#         self.week = data['week']
#         self.date = data['start_date']
#         self.venue = data['venue']
#         self.home_team_name = data['home_team']
#         self.away_team_name = data['away_team']
#         self.scores = {data['home_id']: data['home_points'],
#                        data['away_id']: data['away_points']}
        
#     # This method gets called whenever we try to print a Game object
#     def __str__(self):
#         return f"Game(id='{self.id}', season='{self.season}', week='{self.week}', matchup='{self.away_team_name} vs. {self.home_team_name}')"


def read_in_games_data():
    # open and read games data file
    with open('2022_games_data.json') as file:
        games_data = json.load(file)

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

        session.commit()