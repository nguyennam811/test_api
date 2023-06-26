from ..database import Base
from sqlalchemy import Column, String, JSON
import uuid
from uuid import UUID

class Device(Base):
    __tablename__ = 'Device'
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    other_statuses = Column(JSON, nullable=True)