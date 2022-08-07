from dataclasses import dataclass
import uuid
import re
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from fastapi import HTTPException
from typing import get_type_hints

from util.crypto import get_password_hash


email_reg= re.compile("^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")

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
    verified: bool = False

    def __init__(self,**data):
        super().__init__(**data)
        self.validate()
        self.hashing_password()

    def validate(self):
        #uuid validation
        #password validation
        print("validate")
        class_name = self.__class__.__name__.lower()
        type_hints = get_type_hints(self)
        for var in User.__fields__.keys():
            var_instancce = getattr(self, var)
            if not isinstance(var_instancce, type_hints[var]):
                raise HTTPException(status_code=400, detail=f"TypeError: {class_name}.{var} must be {type_hints[var]} not {type(var)}")

        if not email_reg.match(self.email):
            raise HTTPException(status_code=400, detail="Invalidation Model: user.email")

        if self.student_id < 201400000:
            raise HTTPException(status_code=400, detail="Invalidation Model: user.student_id")

    def hashing_password(self):
        self.password = get_password_hash(self.password)

    def to_view_model(self):
        print(self.id,self.name)
        return User1(id=self.id,name=self.name)

class User1(BaseModel):
    id: uuid.UUID
    name: str