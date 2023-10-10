from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.db.database import get_db
from app.schemas.choices import ChoiceGet
from app.services.choice_service import ChoiceService


router = APIRouter(prefix="/choice", tags=["Choices"])


@router.get("/get_by_choice_id", response_model=ChoiceGet)
async def get_by_id(choice_id: UUID, db: AsyncSession = Depends(get_db)):
    Service = ChoiceService(db=db)
    return await Service.get_by_id(id=choice_id)


@router.get("/get_by_scene_id", response_model=list[ChoiceGet])
async def get_choices_by_scene_id(scene_id: UUID, db: AsyncSession = Depends(get_db)):
    Service = ChoiceService(db=db)
    return await Service.get_all_by_scene_id(scene_id=scene_id)


@router.get("/get_by_game_id", response_model=list[ChoiceGet])
async def get_choices_by_game_id(game_id: UUID, db: AsyncSession = Depends(get_db)):
    Service = ChoiceService(db=db)
    return await Service.get_all_by_game_id(game_id=game_id)
