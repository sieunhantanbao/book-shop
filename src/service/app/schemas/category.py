from sqlalchemy import Column, Integer, String
from database import Base
from .base_entity import BaseEntity
from .image import Image
from sqlalchemy.orm import relationship
    
    
class Category(Base, BaseEntity):
    __tablename__ = "categories"
    
    name = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    short_description = Column(String)
    thumbnail_url = Column(String)
    sort_order = Column(Integer, nullable=False, default=0)
    books = relationship('Book', back_populates='category', lazy = 'immediate')
    images = relationship('Image', back_populates='category', lazy = 'immediate')
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}