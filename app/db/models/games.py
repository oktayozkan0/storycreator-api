from app.db.models.base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Games(Base):
    title = Column(String(50), nullable=False)
    thumbnail = Column(String)

    scenes = relationship("Scenes", back_populates="games")
