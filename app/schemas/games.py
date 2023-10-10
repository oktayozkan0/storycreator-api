import uuid
from pydantic import AfterValidator, BaseModel, HttpUrl
from typing import Annotated


HttpUrlString = Annotated[
    HttpUrl, AfterValidator(lambda v: str(v) if v is not None else v)
]


class GameBase(BaseModel):
    title: str
    thumbnail: HttpUrlString | None = None


class GameCreate(GameBase):
    pass


class GameGet(GameBase):
    id: uuid.UUID


class GameUpdate(BaseModel):
    title: str | None = None
    thumbnail: HttpUrlString | None = None
