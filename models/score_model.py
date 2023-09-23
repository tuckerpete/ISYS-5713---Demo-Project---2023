from models import base_model

from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


# The Team class hold information about team objects
class Score(base_model.Base):
    __tablename__ = 'score'

    game_id: Mapped[int] = mapped_column(ForeignKey("game.id"), primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("team.id"), primary_key=True)
    team_side: Mapped[str] # 'Home' or 'Away'
    points: Mapped[Optional[int]]

    team: Mapped["Team"] = relationship(back_populates="scores")
    game: Mapped["Game"] = relationship(back_populates="scores")