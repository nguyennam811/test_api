from pydantic import BaseModel
from typing import Optional, Any
from .Schemas_DeviceTypes import ShowDeviceTypes
from .Schemas_DeviceGroupsType import ShowDeviceGroupsType
from .Schemas_Device import ShowDevice

class ResponseSchema(BaseModel):
    result: Optional[Any] = None

class PageResponse(BaseModel):
    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: list[ShowDeviceGroupsType] | list[ShowDeviceTypes] | list[Any]


class DeviceResponse(BaseModel):
    context: str
    value: list[ShowDevice]
    nextLink: str
