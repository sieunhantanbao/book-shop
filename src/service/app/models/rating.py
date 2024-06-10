from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class UserInRatingViewModel(BaseModel):
    first_name: str
    last_name: str
    class ConfigDict:
        from_attributes = True
        
class BookRatingViewModel(BaseModel):
    id: UUID
    user_id: UUID
    book_id: UUID
    rating_value: float
    comment: str
    is_reviewed: bool
    created_at: datetime
    user: Optional[UserInRatingViewModel]
    class ConfigDict:
        from_attributes: True
        

class BookReviewCreateModel(BaseModel):
    book_id: UUID
    rating_value: float
    review_comment: Optional[str] = None
