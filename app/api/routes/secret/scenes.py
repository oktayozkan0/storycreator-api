from app.db.database import get_db
from app.schemas.scenes import SceneBase, SceneResponse
from app.services.scene_service import SceneService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


router = APIRouter(prefix="/scene", tags=["Scenes"])


@router.post("/create", response_model=SceneResponse)
async def create_scene(
    game_id: UUID, payload: SceneBase, db: AsyncSession = Depends(get_db)
):
    Service = SceneService(db=db)
    res = await Service.create(payload=payload, game_id=game_id)
    return res


@router.post("/update", response_model=SceneResponse)
async def update_scene(
    scene_id: UUID, payload: SceneBase, db: AsyncSession = Depends(get_db)
):
    Service = SceneService(db=db)
    res = await Service.update(id=scene_id, payload=payload)
    return res


@router.delete("/delete")
async def delete_scene(scene_id: UUID, db: AsyncSession = Depends(get_db)):
    Service = SceneService(db)
    res = await Service.delete(id=scene_id)
    return res
