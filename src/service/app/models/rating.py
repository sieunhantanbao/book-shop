from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from typing import Optional

class BookRatingViewModel(BaseModel):
    id: UUID
    user_id: UUID
    book_id: UUID
    rating_value: float
    comment: str
    is_reviewed: bool
    created_at: datetime
    class Config:
        orm_mode: True
        

class BookReviewCreateModel(BaseModel):
    book_id: UUID
    rating_value: float
    review_comment: Optional[str] = None