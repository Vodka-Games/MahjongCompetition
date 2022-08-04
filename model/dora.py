import uuid
from sqlmodel import Field, SQLModel


class Dora(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    game_id: uuid.UUID = Field(default=None, foreign_key="game.id",nullable=False)
    dora: int
    order: int
