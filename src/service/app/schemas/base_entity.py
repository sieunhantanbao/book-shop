import uuid
from sqlalchemy import Column, Time, UUID
from datetime import datetime

class BaseEntity:
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    created_at = Column(Time, nullable=False, default=datetime.now())
    updated_at = Column(Time, nullable=True)