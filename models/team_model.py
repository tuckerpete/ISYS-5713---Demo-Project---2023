import json

from models import base_model
from models.score_model import Score

from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

# The Team class hold information about team objects
class Team(base_model.Base):
    __tablename__ = 'team'

    id: Mapped[int] = mapped_column(primary_key=True)
    school: Mapped[str]
    mascot: Mapped[Optional[str]]
    abbreviation: Mapped[Optional[str]]
    conference: Mapped[Optional[str]]
    color: Mapped[Optional[str]]
    alt_color: Mapped[Optional[str]]

    scores: Mapped[List["Score"]] = relationship(back_populates="team")

    def __repr__(self) -> str:
        return f"Team(id='{self.id}', school='{self.school}', conference='{self.conference}')"

### OLD Team Class
# class Team:
#     # This method gets called when a new Team is created. Data from the data file will be passed to this method
#     def __init__(self, data):
#         self.id = data['id']
#         self.school = data['school']
#         self.mascot = data['mascot']
#         self.abbreviation = data['abbreviation']
#         self.conference = data['conference']
#         self.color = data['color']
#         self.alt_color = data['alt_color']
#         self.logo = None
#         if data['logos'] is not None:
#             self.logo = data['logos'][0]
#         self.games = []
#         self.ppg = 0

#     # This method adds a Game object to the "games" list of this Team object and then calculates the team's PPG
#     def add_game(self, game):
#         self.games.append(game)
#         self.calculate_ppg()

#     # This method calculates the team's average points-per-game (ppg)
#     def calculate_ppg(self):
#         scores = []
#         for game in self.games:
#             points = game.scores[self.id]
#             if points is not None:
#                 scores.append(points)
#         if len(scores) > 0:
#             self.ppg = round(sum(scores)/len(scores), 2)

#     # This method gets called whenever we try to print a Team object
#     def __str__(self):
#         return f"Team(id='{self.id}', school='{self.school}', conference='{self.conference}')"
    


def read_in_teams_data():
    # open and read teams data file
    with open('teams_data.json') as file:
        teams_data = json.load(file)

    # teams = {'team_id': Team object}   <-- This will hold our Teams objects
    teams = {}

    # loop through the teams in the data file and create Team objects
    for team_data in teams_data:
        teams[team_data['id']] = Team(team_data)

    return teams


def rank_teams_by_ppg(teams):
    # order the teams by most to least ppg
    teams_sorted_by_ppg = sorted(teams.values(), key=lambda team: team.ppg, reverse=True)
    return teams_sorted_by_ppg