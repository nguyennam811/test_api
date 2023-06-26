from ..database import Base
from sqlalchemy import Boolean, Column, String, DateTime, func
import uuid

class User(Base):
    __tablename__ = 'users'

    sub = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    last_requested_time = Column(String)
    email_verified = Column(String)
    phone_number_verified = Column(String)
    old_sub = Column(String)
    name = Column(String)
    phone_number = Column(String)
    nd_requests = Column(String)
    nm_requests = Column(String)
    app_key = Column(String, default=lambda: str(uuid.uuid4()))
    email = Column(String)
    enabled = Column(Boolean)
    status = Column(String)
    created = Column(DateTime(timezone=True), default=func.now())
    updated = Column(DateTime(timezone=True), default=func.now(),  onupdate=func.now())

    # address = Column(String)
    # config = Column(JSON)