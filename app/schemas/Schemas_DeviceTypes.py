from pydantic import BaseModel
from .Schemas_Chip import Chip
from typing import Optional
import datetime

class DeviceTypes(BaseModel):
    name: str
    description: str
    type_number: int
    model_name: str
    manufacturer_name: str
    updated: Optional[str] | None


class ShowDeviceTypes(DeviceTypes):
    id: str
    chip_id: str
    device_group_type_id: str
    created: Optional[datetime.datetime]
    chip: Chip
    class Config():
        orm_mode = True


