from app.db.models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Scenes(Base):
    scene_text = Column(String)
    scene_img = Column(String)
    scene_title = Column(String)

    game_id = Column(UUID(as_uuid=True), ForeignKey("games.id"))

    games = relationship("Games", back_populates="scenes")
