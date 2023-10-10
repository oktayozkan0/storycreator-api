from app.db.database import get_db
from app.schemas.games import GameCreate, GameGet, GameUpdate
from app.services.game_service import GameService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


router = APIRouter(prefix="/game", tags=["Games"])


@router.post("/create", response_model=GameGet)
async def create_game(payload: GameCreate, db: AsyncSession = Depends(get_db)):
    """
    create game
    """
    Service = GameService(db)
    return await Service.create(payload=payload)


@router.post("/update", response_model=GameGet)
async def update_game(
    game_id: UUID,
    payload: GameUpdate,
    db: AsyncSession = Depends(get_db),
):
    """
    update a game by id
    """
    Service = GameService(db)
    return await Service.update(id=game_id, payload=payload)


@router.delete("/delete")
async def delete_game(game_id: UUID, db: AsyncSession = Depends(get_db)):
    Service = GameService(db)
    res = await Service.delete(id=game_id)
    return res
