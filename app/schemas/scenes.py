from pydantic import AfterValidator, BaseModel, HttpUrl
from typing import Annotated
from uuid import UUID


HttpUrlString = Annotated[
    HttpUrl, AfterValidator(lambda v: str(v) if v is not None else v)
]


class SceneBase(BaseModel):
    scene_text: str | None = None
    scene_img: HttpUrlString | None = None
    scene_title: str


class SceneResponse(SceneBase):
    id: UUID
