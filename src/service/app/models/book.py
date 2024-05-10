from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, field_validator
from models.image import ImageViewModel
from models.rating import BookRatingViewModel

class BaseBookViewModel:
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
    

class BookRelatedViewModel(BaseModel, BaseBookViewModel):
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    
    class Config:
        orm_mode: True

class BookDetailViewModel(BaseModel, BaseBookViewModel):
    book_comments: Optional[List[BookRatingViewModel]] = None
    books_in_cat: Optional[List[BookRelatedViewModel]] = None
    related_books: Optional[List[BookRelatedViewModel]] = None
    user_wishlists: Optional[List[UUID]] = None
    rating_statistic: Optional[dict[str, float]] = None
    
    class Config:
        orm_mode: True
        
class BookFeaturedViewModel(BaseModel):
    id: UUID
    title: str
    slug: str
    short_description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    sort_order: Optional[int] = 0
    category_id: UUID
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    
    class Config:
        orm_mode: True
        

class BookFilterInputModel(BaseModel):
    keyword: Optional[str] = None
    category_ids: Optional[List[UUID]] = None
    min_price_input: float
    max_price_input: float
    min_rate_input: int
    max_rate_input: int
    sort_by: Optional[str] = None

    @field_validator('min_rate_input', 'max_rate_input')
    def validate_rating_range(cls, v):
        if v < 0 or v > 5:
            raise ValueError('Rating must be between 0 and 5')
        return v

    # @field_validator('max_rate_input')
    # def validate_rating_order(cls, v, values, **kwargs):
    #     min_rate_input = values.get('min_rate_input')
    #     if min_rate_input is not None and v < min_rate_input:
    #         raise ValueError('max_rate_input must be greater than or equal to min_rate_input')
    #     return v

    @field_validator('min_price_input', 'max_price_input')
    def validate_price_range(cls, v):
        if v < 0:
            raise ValueError('Price must be non-negative')
        return v

    # @field_validator('max_price_input')
    # def validate_price_order(cls, v, values, **kwargs):
    #     min_price_input = values.get('min_price_input')
    #     if min_price_input is not None and v < min_price_input:
    #         raise ValueError('max_price_input must be greater than or equal to min_price_input')
    #     return v

    