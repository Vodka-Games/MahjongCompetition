import uuid
from sqlmodel import Field, SQLModel

class MatchPlayer(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    match_id: uuid.UUID = Field(default=None, foreign_key="match.id",nullable=False)
    user_id: uuid.UUID = Field(default=None, foreign_key="user.id",nullable=False)
    seat: int