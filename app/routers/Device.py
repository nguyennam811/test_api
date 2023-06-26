from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from ..schemas import Schemas_Device, Schemas
from ..database import get_db
from ..repository import Device

router = APIRouter(
    prefix="/device",
    tags=["Devices"]
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=Schemas.DeviceResponse)
async def get_user(db: Session = Depends(get_db)):
    return Device.get_device_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request: Schemas_Device.Device, db: Session = Depends(get_db)):
    return Device.create_device(request, db)
