from app.db.models.scenes import Scenes
from app.services.base_service import BaseService, select
from sqlalchemy.ext.asyncio import AsyncSession


class SceneService(BaseService):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db)
        self.model: Scenes = Scenes

    async def get_by_game_id(self, game_id):
        stmt = select(self.model).where(self.model.game_id == game_id)
        result = await self.db.execute(stmt)
        instance = result.scalars().all()
        return instance
