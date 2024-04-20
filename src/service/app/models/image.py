from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class ImageViewModel(BaseModel):
    id: UUID
    book_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    url: str
    
    class Config:
        orm_mode: True