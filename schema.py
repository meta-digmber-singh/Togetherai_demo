from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class QueryRequest(BaseModel):
    prompt: str
    realtime: Optional[bool] = False


class QueryResponce(QueryRequest):
    id: int
    responce: str
    created_at: datetime

    class config:
        orm_mode = True
    