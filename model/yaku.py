import uuid
from typing import Optional
from sqlmodel import Field, SQLModel

class Yaku(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    result_id: uuid.UUID = Field(default=None, foreign_key="result.id",nullable=False)
    name: str
    yakuman: bool
    han: int
    fu: Optional[int]