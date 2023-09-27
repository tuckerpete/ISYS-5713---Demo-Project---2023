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


def read_in_teams_data():
    # open and read teams data file
    with open('teams_data.json') as file:
        teams_data = json.load(file)

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




def rank_teams_by_ppg():
    # order the teams by most to least ppg
    with Session(base_model.engine) as session:
        teams_sorted_by_ppg = session.query(Team.school, func.avg(Score.points)).join(Score).group_by(Team.id).order_by(func.avg(Score.points).desc()).all()
    return teams_sorted_by_ppg


# select Team.school, avg(Score.points) as ppg
# from Team
# join Score on Team.id = Score.team_id
# group by Team.id, Team.school
# order by avg(Score.points) desc

