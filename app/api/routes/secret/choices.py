from app.db.database import get_db
from app.schemas.choices import ChoiceCreate, ChoiceGet
from app.services.choice_service import ChoiceService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


router = APIRouter(prefix="/choice", tags=["Choices"])


@router.post("/create", response_model=ChoiceGet)
async def create_choice(
    payload: ChoiceCreate, game_id: UUID, db: AsyncSession = Depends(get_db)
):
    Service = ChoiceService(db=db)
    res = await Service.create(payload=payload, game_id=game_id)
    return res


@router.post("/update", response_model=ChoiceCreate)
async def update_choice(
    choice_id: UUID, payload: ChoiceCreate, db: AsyncSession = Depends(get_db)
):
    Service = ChoiceService(db=db)
    res = await Service.update(id=choice_id, payload=payload)
    return res


@router.delete("/delete")
async def delete_choice(choice_id: UUID, db: AsyncSession = Depends(get_db)):
    Service = ChoiceService(db)
    res = await Service.delete(id=choice_id)
    return res
