import uuid
from typing import Optional
from sqlmodel import Field, SQLModel

class Game(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    match_id: uuid.UUID = Field(default=None, foreign_key="match.id",nullable=False)
    wind: int
    seat: int
    honba: int
    continuation: int
    method: int #tsumo/ron/draw/chunbo
    reason: Optional[str]
