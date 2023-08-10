from pydantic import BaseModel


class TestData(BaseModel):
    id: str
    name: str
    pass
