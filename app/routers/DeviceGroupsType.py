from fastapi import APIRouter, status, Depends, Query
from ..schemas import Schemas_DeviceGroupsType, Schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import DeviceGroupsType

# from fastapi_pagination import add_pagination, Page, paginate


router = APIRouter(
    prefix="/devicegroupstype",
    tags=['DeviceGroupsType']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=Schemas.ResponseSchema)
async def get_device_groups_type(
        db: Session = Depends(get_db),
        filters: str = Query(None, min_length=1, max_length=100),
        search: str = Query(None, min_length=1, max_length=100),
        sort: str = Query(None, min_length=1, max_length=100),
        page: int = Query(1, ge=1),
        limit: int = Query(5, ge=1, le=100)
):
    result = DeviceGroupsType.get_device_groups_type_all(db, filters, search, sort, page, limit)
    return Schemas.ResponseSchema(result=result)




