from pydantic import BaseModel
from .Schemas_DeviceTypes import ShowDeviceTypes
from typing import Optional
import datetime

class DeviceGroupsType(BaseModel):
    name: str
    group_type_number: int
    image_uri: str
    updated: str | None

class ShowDeviceGroupsType(DeviceGroupsType):
    id: str
    created: Optional[datetime.datetime]
    device_types: list[ShowDeviceTypes] = []
    class Config():
        orm_mode = True