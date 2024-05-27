from sqlalchemy import Boolean, Column, Float, ForeignKey, String, UUID
from app.database import Base
from .base_entity import BaseEntity
from sqlalchemy.orm import relationship
from .book import Book

class Rating(Base, BaseEntity):
    __tablename__ = "ratings"
    
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    book_id = Column(UUID, ForeignKey('books.id'), nullable=False)
    rating_value  = Column(Float, nullable=False)
    comment = Column(String)
    is_reviewed = Column(Boolean, default = False, nullable=False)
    user = relationship("User")
    book = relationship("Book")
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}