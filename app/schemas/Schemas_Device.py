from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Device(BaseModel):

    other_statuses: Optional[dict[str, Optional[bool]]]

class ShowDevice(Device):
    id: UUID
    class Config():
        orm_mode = True
