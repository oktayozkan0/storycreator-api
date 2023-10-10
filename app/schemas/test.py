import uuid
from pydantic import BaseModel


class TestCreateSchema(BaseModel):
    test_col: str


class TestUpdateSchema(BaseModel):
    id: uuid.UUID
    new_col: str
