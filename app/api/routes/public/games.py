from app.db.database import get_db
from app.schemas.games import GameGet
from app.services.game_service import GameService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


router = APIRouter(prefix="/game", tags=["Games"])


@router.get("/get_games", response_model=list[GameGet])
async def get_games(db: AsyncSession = Depends(get_db)):
    Service = GameService(db=db)
    return await Service.get_all()


@router.get("/get", response_model=GameGet)
async def get_game_by_id(game_id: UUID, db: AsyncSession = Depends(get_db)):
    """
    returns a game by id
    """
    Service = GameService(db=db)
    res = await Service.get_by_id(id=game_id)
    return res
