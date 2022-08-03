import uuid
from sqlmodel import Field, SQLModel

class Game(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    competition_id: uuid.UUID = Field(default=None, foreign_key="competition.id",nullable=False)
    wind: int
    seat: int
    continuation: int
    dora: str
    method: int