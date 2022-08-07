from dataclasses import dataclass
from typing import List
import uuid
import datetime
from sqlmodel import Field, SQLModel
from pydantic import BaseModel
from model.user import User1

class Match(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    start_date: datetime.datetime
    end_date: datetime.datetime = Field(default= None, nullable=True)
    competition_id: uuid.UUID = Field(default=None, foreign_key="competition.id",nullable=True)

    def to_view_model(self,user_models):
        user_view_model = [user_model.to_view_model() for user_model in user_models]
        return Match1(id=self.id,start_date=self.start_date,end_date=self.end_date,players=user_view_model)

class Match1(BaseModel):
    id: uuid.UUID
    start_date: datetime.datetime
    end_date: datetime.datetime | None
    players: list[User1]
