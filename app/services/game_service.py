from app.db.models.games import Games
from app.services.base_service import BaseService
from sqlalchemy.ext.asyncio import AsyncSession


class GameService(BaseService):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(db)
        self.model = Games
