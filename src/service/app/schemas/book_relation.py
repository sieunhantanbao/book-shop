from sqlalchemy import UUID, Column, ForeignKey, Integer
from app.database import Base
from .base_entity import BaseEntity
    
class BookRelation(Base, BaseEntity):
    __tablename__ = "book_relations"
    
    book_id_1 = Column(UUID, ForeignKey('books.id'), nullable=False)
    book_id_2 = Column(UUID, ForeignKey('books.id'), nullable=False)
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}