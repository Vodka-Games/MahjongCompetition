from database import create_db_and_tables

from model.user import *
from fastapi import Depends, FastAPI, HTTPException, status

from controller import match, user

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(user.router,prefix="/api/v1",)
app.include_router(match.router,prefix="/api/v1",)