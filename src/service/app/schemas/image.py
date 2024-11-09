from sqlalchemy import Column, ForeignKey, String, UUID
from app.database import Base
from .base_entity import BaseEntity
from sqlalchemy.orm import relationship
    
class Image(Base, BaseEntity):
    __tablename__ = "images"
    
    book_id = Column(UUID, ForeignKey('books.id'), nullable=True)
    category_id = Column(UUID, ForeignKey('categories.id'), nullable=True)
    url = Column(String)
    category = relationship("Category")
    book = relationship("Book")
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}