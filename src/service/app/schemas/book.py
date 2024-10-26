from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Time, UUID
from database import Base
from .base_entity import BaseEntity
from sqlalchemy.orm import relationship
from .category import Category    
from .image import Image   
    
class Book(Base, BaseEntity):
    __tablename__ = "books"

    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    short_description = Column(String)
    description = Column(String)
    price = Column(Float, nullable=False)
    isbn = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String)
    publish_date = Column(Time)
    pages = Column(Integer)
    dimensions = Column(String)
    language = Column(String)
    thumbnail_url = Column(String)
    sort_order = Column(Integer, default=0)
    is_featured = Column(Boolean, nullable=False, default = False)
    is_published = Column(Boolean, nullable=False, default = False)
    category_id = Column(UUID, ForeignKey('categories.id'), nullable=False)
    category = relationship("Category")
    ratings = relationship('Rating', back_populates='book', lazy = 'immediate')
    images = relationship('Image', back_populates='book', lazy = 'immediate')
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    