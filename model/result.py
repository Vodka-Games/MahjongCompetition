import uuid
from sqlmodel import Field, SQLModel

class Result(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    game_id: uuid.UUID = Field(default=None, foreign_key="game.id",nullable=False)
    winner_id: uuid.UUID= Field(default=None, foreign_key="user.id",nullable=False)
    loser_id: uuid.UUID= Field(default=None, foreign_key="user.id",nullable=False)
    oya: bool
    han: int
    fu: int
    pass_score: int
    dora: int