from sqlmodel import  SQLModel, create_engine,Session,select
from model.user import *
from model import competition,dora,game,player,result,resultyaku,user,player,yaku
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from util.crypto import encrypt,decrypt
from util.mail import send_mail

from base64 import b64decode

import secret


engine = create_engine(secret.mysql_connection_string,echo=True)
SQLModel.metadata.create_all(engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

class RegisterParam(BaseModel):
    name: str
    student_id: int
    password: str
    email: str


@app.post("/signup")
async def registerUser(param : RegisterParam):

    user = User(**vars(param))

    with Session(engine) as session:
        statement = select(User).where(User.email == user.email)
        results = session.exec(statement)
        if results.one_or_none() != None:
            raise HTTPException(status_code=400, detail="The email is already signed up.")
        
    nonce, ciphertext, tag = encrypt(str(user.id))
    
    mail_param = {
        "nonce": nonce,
        "tag": tag,
        "id": ciphertext
    }
    await send_mail("/signup/verify",mail_param,user.email)

    with Session(engine) as session:
        session.add(user)
        session.commit()
    return {"message": "email has been sent"}

@app.get("/signup/verify")
async def verifyUser(id: str = '',nonce:str='',tag:str=''):
    id = b64decode(id)
    nonce = b64decode(nonce)
    tag = b64decode(tag)

    decrypted_id = decrypt(nonce,id,tag)
    
    with Session(engine) as session:
        statement = select(User).where(User.id == decrypted_id)
        results = session.exec(statement)
        user = results.one()
        user.verified = True
        session.add(user)
        session.commit()

    return {"message": "success"}
    