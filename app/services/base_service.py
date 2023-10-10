from app.db.models.base import Base
from datetime import datetime
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID


class BaseService:
    def __init__(self, db: AsyncSession) -> None:
        self.model: Base
        self.db = db

    async def get_all(self):
        stmt = select(self.model).where(self.model.is_active == True)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def get_by_id(self, id: UUID):
        stmt = select(self.model).where(self.model.id == id)
        result = await self.db.execute(stmt)
        instance = result.scalars().first()
        if not instance:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Not Found"
            )
        return instance

    async def create(self, payload: BaseModel, **kwargs):
        data = self.model(**payload.model_dump(exclude_none=True), **kwargs)
        self.db.add(data)
        await self.db.commit()
        return data

    async def update(self, id: UUID, payload: BaseModel):
        instance = await self.get_by_id(id)
        dct = payload.model_dump(exclude_none=True)
        update_stmt = update(self.model).where(self.model.id == id).values(**dct)
        await self.db.execute(update_stmt)
        await self.db.commit()
        return instance

    async def delete(self, id: UUID):
        try:
            update_stmt = (
                update(self.model)
                .where(self.model.id == id)
                .values(is_active=False, deleted_at=datetime.now())
            )
            await self.db.execute(update_stmt)
            await self.db.commit()
            return HTTPException(
                status_code=status.HTTP_204_NO_CONTENT, detail="Deleted"
            )
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Something went wrong.",
            )
