from base64 import b64decode
from datetime import timedelta

from fastapi import HTTPException,status
from sqlmodel import select
from passlib.context import CryptContext
from authorization.handler import authenticate_user, create_access_token 

from model.user import User

from database import get_db_session

from util.crypto import decrypt, encrypt, verify_password,get_password_hash
from util.mail import send_mail
from secret import access_token_expire_minutes

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    async def register_user(name: str,student_id: int,password: str,email: str):
        user = User(name=name,student_id=student_id,password=password,email=email)

        with get_db_session() as session:
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
        await send_mail("/api/v1/user/signup/verify",mail_param,user.email)

        with get_db_session() as session:
            session.add(user)
            session.commit()

        return {"message": "email has been sent"}

    async def verify_user(id: str,nonce:str,tag:str):
        id = b64decode(id)
        nonce = b64decode(nonce)
        tag = b64decode(tag)

        decrypted_id = decrypt(nonce,id,tag)

        with get_db_session() as session:
            statement = select(User).where(User.id == decrypted_id)
            results = session.exec(statement)
            user = results.one()
            user.verified = True
            session.add(user)
            session.commit()

        return {"message": "your account has been successfully created."}

    async def login(email:str, password: str):
        user = authenticate_user(email, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    