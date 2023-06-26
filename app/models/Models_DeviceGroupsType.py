from ..database import Base
from sqlalchemy import Column, String, DateTime, func, Integer
import uuid
from sqlalchemy.orm import relationship

class DeviceGroupsType(Base):
    __tablename__ = 'devicegroupstype'
    name = Column(String)
    group_type_number = Column(Integer)
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    image_uri = Column(String)
    created = Column(DateTime(timezone=True), default=func.now())
    # updated = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    updated = Column(String)

    device_types = relationship("DeviceTypes", back_populates='device_type')