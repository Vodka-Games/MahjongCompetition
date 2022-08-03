from sqlmodel import  SQLModel, create_engine

from model import user, competition, game

engine = create_engine('mysql://root:admin@localhost:3307/mahjong',echo=True)
SQLModel.metadata.create_all(engine)
    