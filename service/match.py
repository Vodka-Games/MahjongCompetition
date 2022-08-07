

from datetime import datetime
from typing import List
import uuid
from fastapi import HTTPException,status
from database import get_by_id, get_db_session
from model.match import Match
from model.matchplayer import MatchPlayer
from model.user import User

class MatchService():
    async def create_match(player_id_list: List[uuid.UUID]):
        match_model = Match(start_date=datetime.now(),end_date=None,competition_id=None)
        # 안 끝났는데 대회 하는 놈 컷
        if len(player_id_list) != len(set(player_id_list)):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="InvalidationRequest: Duplicate user.id")
        users = []
        for player_id in player_id_list:
            user = get_by_id(User,player_id)
            if not user:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="InvalidationRequest: user does not exist")
            users.append(user)

        match_player_models = [MatchPlayer(match_id=match_model.id,seat=i, user_id=player_id) for i, player_id in enumerate(player_id_list)]
        
        with get_db_session()  as session:
            session.add(match_model)
            session.add_all(match_player_models)

            session.commit()
            session.refresh(match_model)
    
        return match_model.to_view_model(users)
