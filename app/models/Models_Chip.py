from ..database import Base
from sqlalchemy import Column, String
import uuid
from sqlalchemy.orm import relationship


class Chip(Base):
    __tablename__ = 'chip'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String)
    module = Column(String)

    chip_device_type = relationship("DeviceTypes", back_populates='chip')