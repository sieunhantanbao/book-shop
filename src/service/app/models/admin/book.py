from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, field_validator
from app.models.image import ImageViewModel

class BaseAdminBookViewModel(BaseModel):
    id: UUID
    title: str
    slug: str
    short_description: Optional[str] = None
    description: Optional[str] = None
    price: float
    isbn: str
    author: str
    publisher: Optional[str] = None
    publish_date: Optional[datetime] = None
    pages: int
    dimensions: Optional[str] = None
    language: Optional[str] = None
    thumbnail_url: Optional[str] = None
    sort_order: Optional[int] = 0
    is_featured: Optional[bool] = False
    is_published: Optional[bool] = False
    category_id: UUID
    average_rating_value: Optional[float] = None
    total_ratings: Optional[int] = None
    in_wishlist: Optional[bool] = None
    images: Optional[List[ImageViewModel]] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class ConfigDict:
        from_attributes: True

class AdminBookCreateOrUpdateRequestModel(BaseModel):
    id: Optional[UUID] = None
    title: str
    short_description: Optional[str] = None
    description: Optional[str] = None
    price: float
    isbn: str
    author: str
    publisher: Optional[str] = None
    publish_date: Optional[datetime] = None
    pages: int
    dimensions: Optional[str] = None
    language: Optional[str] = None
    thumbnail_url: Optional[str] = None
    sort_order: Optional[int] = 0
    is_featured: Optional[bool] = False
    is_published: Optional[bool] = False
    category_id: UUID
    
    @field_validator('pages')
    def check_pages(cls, v):
        if v <= 0:
            raise ValueError("The number of pages must be greater than zero")
        return v

    class ConfigDict:
        validate_assignment = True