from sqlmodel import  SQLModel, create_engine
from model import competition,dora,game,player,result,resultyaku,user,player,yaku

engine = create_engine('mysql://root:admin@localhost:3307/mahjong',echo=True)
SQLModel.metadata.create_all(engine)
    