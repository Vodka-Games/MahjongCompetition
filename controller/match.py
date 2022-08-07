from typing import List
import uuid
from fastapi import APIRouter,Header,Depends,Query
from pydantic import BaseModel
from authorization.handler import get_current_user
from model.user import User
from service.match import MatchService

router = APIRouter(
    prefix="/match",
    tags=["match"],
    dependencies=[],
)

#createGame
#getGame
#deleteGame
class CreateMatchParam(BaseModel):
    player_ids: list[uuid.UUID]

@router.post("/",dependencies=[Depends(get_current_user)])
async def create_match(param:CreateMatchParam):
    return await MatchService.create_match(param.player_ids)