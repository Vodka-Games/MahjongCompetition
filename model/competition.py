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
    date: datetime.date
