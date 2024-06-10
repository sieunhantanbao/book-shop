from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class BaseAdminRatingViewModel(BaseModel):
    id: UUID
    user_id: UUID
    book_id: UUID
    rating_value: float
    comment: str
    is_reviewed: bool
    created_at: datetime
    updated_at: datetime
    class ConfigDict:
        from_attributes: True
