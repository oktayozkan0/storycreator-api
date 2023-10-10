from app.db.models.choices import Choices
from app.services.base_service import BaseService, select
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


class ChoiceService(BaseService):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db)
        self.model: Choices = Choices

    async def get_all_by_scene_id(self, scene_id):
        stmt = select(self.model).where(self.model.scene_id == scene_id)
        result = await self.db.execute(stmt)
        instance = result.scalars().all()
        return instance

    async def get_all_by_game_id(self, game_id: UUID):
        stmt = select(self.model).where(self.model.game_id == game_id)
        result = await self.db.execute(stmt)
        instance = result.scalars().all()
        return instance
