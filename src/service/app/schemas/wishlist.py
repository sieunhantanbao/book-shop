from sqlalchemy import Column, ForeignKey, UUID
from app.database import Base
from .base_entity import BaseEntity
    
class WishList(Base, BaseEntity):
    __tablename__ = "wishlists"
    
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    book_id = Column(UUID, ForeignKey('books.id'), nullable=False)
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}