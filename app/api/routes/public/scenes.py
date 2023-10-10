from app.db.database import get_db
from app.services.scene_service import SceneService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


router = APIRouter(prefix="/scene", tags=["Scenes"])


@router.get("/get")
async def get_all_scenes(game_id: UUID, db: AsyncSession = Depends(get_db)):
    """
    returns all scenes for a game
    """
    Service = SceneService(db)
    result = await Service.get_by_game_id(game_id=game_id)
    return result
