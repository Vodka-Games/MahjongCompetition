import uuid
import re
import hashlib
from sqlmodel import Field, SQLModel, create_engine
from fastapi import HTTPException
from typing import get_type_hints


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
                raise HTTPException(status_code=400, detail=f"TypeError: {class_name}.{var_type} must be {var_type} not {type(var)}")

        if not email_reg.match(self.email):
            raise HTTPException(status_code=400, detail="Invalidation Model: user.email")

        if self.student_id < 201400000:
            raise HTTPException(status_code=400, detail="Invalidation Model: user.student_id")

    def hashing_password(self):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
