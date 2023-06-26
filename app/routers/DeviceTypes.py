from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import DeviceTypes
from ..schemas import Schemas_DeviceTypes, Schemas
# from fastapi_pagination import add_pagination, Page, paginate

router = APIRouter(
    prefix="/devicetypes",
    tags=['DeviceTypes']
)

# @router.get('/', status_code=status.HTTP_200_OK, response_model= list[Schemas_DeviceTypes.ShowDeviceTypes])
# async def get_device_types(db: Session = Depends(get_db)):
#     return DeviceTypes.get_device_types_all(db)

@router.get('/', status_code=status.HTTP_200_OK, response_model=Schemas.ResponseSchema)
async def get_device_types(
        db: Session = Depends(get_db),
        columns: str = Query(None, min_length=1, max_length=100),
        search: str = Query(None, min_length=1, max_length=100),
        filter: str = Query(None, min_length=1, max_length=100),
        sort: str = Query(None, min_length=1, max_length=100),
        page: int = Query(1, ge=1),
        limit: int = Query(10, ge=1, le=100),
):

    # return paginate(DeviceTypes.get_device_types_all(db, search, sort))
    result = DeviceTypes.get_device_types_all(db, columns, search, filter, sort, page, limit)
    return Schemas.ResponseSchema(result=result)


