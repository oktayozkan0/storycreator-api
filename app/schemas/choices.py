from pydantic import BaseModel
from uuid import UUID


class ChoiceCreate(BaseModel):
    text: str | None = None
    scene_id: UUID | None = None
    next_scene_id: UUID | None = None


class ChoiceGet(ChoiceCreate):
    id: UUID
