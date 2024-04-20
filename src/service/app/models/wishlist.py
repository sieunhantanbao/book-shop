from datetime import time
from uuid import UUID
from pydantic import BaseModel

class WishlistViewModel(BaseModel):
    id: UUID
    book_id: UUID
    user_id: UUID
    created_date: time
    
    class Config:
        orm_mode: True
