from datetime import datetime
from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from models.book import BookDetailViewModel
from models.image import ImageViewModel

class CategoryViewModel:
    id: UUID
    name: str
    slug: str
    short_description: str
    thumbnail_url: str
    sort_order: int
    images: List[ImageViewModel]
    
    class Config:
        orm_mode: True
        
class CategoryDetailViewModel:
    category: CategoryViewModel
    books: Optional[List[BookDetailViewModel]] = None
    wishlists: Optional[List[UUID]] = None
    def __init__(self, category, books, wishlists: List[UUID]=None) -> None:
        self.category = category
        self.books = books
        self.wishlists = wishlists
        
        
class CategoryView2Model(BaseModel):
    id: UUID
    name: str
    slug: str
    short_description: str
    thumbnail_url: str
    sort_order: int
    images: Optional[List[ImageViewModel]] = None
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    class Config:
        orm_mode: True
    