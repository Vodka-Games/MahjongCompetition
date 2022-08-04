import uuid
from sqlmodel import Field, SQLModel

class Player(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    competition_id: uuid.UUID = Field(default=None, foreign_key="competition.id",nullable=False)
    user_id: uuid.UUID = Field(default=None, foreign_key="user.id",nullable=False)
    seat: int
