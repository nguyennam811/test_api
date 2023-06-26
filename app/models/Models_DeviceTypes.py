from ..database import Base
from sqlalchemy import Column, String, DateTime, func, Integer, ForeignKey
import uuid
from sqlalchemy.orm import relationship

class DeviceTypes(Base):
    __tablename__ = 'devicetypes'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    description = Column(String)
    type_number = Column(Integer)
    chip_id = Column(String, ForeignKey('chip.id'))
    device_group_type_id = Column(String, ForeignKey('devicegroupstype.id'))
    model_name = Column(String)
    manufacturer_name = Column(String)
    created = Column(DateTime(timezone=True), default=func.now())
    # updated = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    updated = Column(String)

    device_type = relationship("DeviceGroupsType", back_populates='device_types')
    chip = relationship("Chip", back_populates='chip_device_type')