from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    content: T
    code: int
    message: Optional[str]
    pass
