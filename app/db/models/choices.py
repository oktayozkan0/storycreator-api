from app.db.models.base import Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Choices(Base):
    text = Column(String)
    scene_id = Column(UUID(as_uuid=True), ForeignKey("scenes.id"))
    next_scene_id = Column(UUID(as_uuid=True), ForeignKey("scenes.id"))
    game_id = Column(UUID(as_uuid=True), ForeignKey("games.id"))

    scenes = relationship("Scenes", foreign_keys=[scene_id])
    scene_next = relationship("Scenes", foreign_keys=[next_scene_id])
    game = relationship("Games", foreign_keys=[game_id])
