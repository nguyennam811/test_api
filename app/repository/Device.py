from sqlalchemy.orm import Session
from ..models import Models_Device
from ..schemas import Schemas_Device, Schemas

def get_device_all(db: Session):
    device = db.query(Models_Device.Device).all()
    # return device
    return Schemas.DeviceResponse(
        context="https://services.odata.org/V4/Northwind/Northwind.svc/$metadata#Customers",
        value=device,
        nextLink="Customers?$skiptoken='ERNSH'"
    )
def create_device(request: Schemas_Device.Device, db: Session):
    # hashedPassword = pwd_context.hash(request.password)
    # request.password = Hash.brypt(request.password)
    new_device = Models_Device.Device(**request.dict())
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device