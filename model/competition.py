import uuid
import datetime
from sqlmodel import Field, SQLModel

class Competition(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    organizer_id: uuid.UUID = Field(default=None, foreign_key="user.id",nullable=False)
    start_date: datetime.datetime
    end_date: datetime.datetime = Field(default= None, nullable=True)
    title: str