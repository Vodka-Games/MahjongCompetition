import uuid
from sqlmodel import Field, SQLModel, create_engine

class User(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str
    student_id: int
    password: str
    email: str
