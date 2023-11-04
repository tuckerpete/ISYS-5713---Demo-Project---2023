import json
import requests

from models import base_model
from models.score_model import Score
from models.game_model import Game

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

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def read_in_teams_data():
    
    # read teams data from API
    base_url = 'https://api.collegefootballdata.com'
    endpoint = '/teams'

    with open('auth_key.txt', 'r') as auth_file:
        auth_key = auth_file.read()

    header = {'Authorization': f'Bearer {auth_key}'}

    response = requests.get(base_url + endpoint, headers=header)

    if response.status_code == 200:
        teams_data = response.json()
    else:
        print(f'ERROR Code {response.status_code} - {response.reason} - {response.text}')
        exit()


    with Session(base_model.engine) as session:
        # find teams already in the database
        existing_teams_objects = session.query(Team).all()
        existing_teams_ids = []
        for team in existing_teams_objects:
            existing_teams_ids.append(team.id)


        # loop through the teams in the data file and create Team objects
        for team_data in teams_data:
            if team_data["id"] not in existing_teams_ids:
                session.add(Team(id=team_data["id"],
                                school=team_data['school'],
                                mascot=team_data['mascot'],
                                abbreviation=team_data['abbreviation'],
                                conference=team_data['conference'],
                                color=team_data['color'],
                                alt_color=team_data['alt_color']))
        
        session.commit()


def rank_teams_by_ppg(conference=None, limit=None, season=None):
    # order the teams by most to least ppg
    with Session(base_model.engine) as session:
        query = session.query(Team.id, Team.school, func.avg(Score.points)).join(Score).join(Game)
        if conference is not None:
            query = query.where(Team.conference==conference)
        if season is not None:
            query = query.where(Game.season==season)
        query = query.group_by(Team.id).order_by(func.avg(Score.points).desc())
        if limit is not None:
            query = query.limit(limit)
        teams_sorted_by_ppg = query.all()
    return teams_sorted_by_ppg


def get_team(team_id):
    with Session(base_model.engine) as session:
        team = session.query(Team).where(Team.id == team_id).first()
    return team

def create_team(team_data):
    with Session(base_model.engine) as session:
        new_team = Team( school=team_data['school'],
                         mascot=team_data['mascot'],
                         abbreviation=team_data['abbreviation'],
                         conference=team_data['conference'],
                         color=team_data['color'],
                         alt_color=team_data['alt_color'])
        session.add(new_team)
        session.commit()
        return new_team
    
def delete_team(team_id):
    team = get_team(team_id)
    if team is not None:
        with Session(base_model.engine) as session:
            session.delete(team)
            session.commit()
        return True
    else:
        return False
    
def update_team(team_id, team_data):
    if get_team(team_id) is not None:
        with Session(base_model.engine) as session:
            session.query(Team).where(Team.id == team_id).update(team_data)
            session.commit()
    return get_team(team_id)

def get_teams(conference=None):
    with Session(base_model.engine) as session:
        teams_query = session.query(Team)
        if conference is not None:
            teams_query = teams_query.where(Team.conference == conference)
        teams = teams_query.all()
    return teams

def get_conference_list():
    with Session(base_model.engine) as session:
        conferences_results = session.query(Team.conference).distinct().order_by(Team.conference).all()
    return [conference[0] for conference in conferences_results]
