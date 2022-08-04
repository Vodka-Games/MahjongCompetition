import uuid
from sqlmodel import Field, SQLModel

class ResultYaku(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    result_id: uuid.UUID = Field(default=None, foreign_key="result.id",nullable=False)
    yaku_id: uuid.UUID = Field(default=None, foreign_key="yaku.id",nullable=False)