from sqlalchemy import Boolean, Column, String, Time
from app.database import Base
from .base_entity import BaseEntity
from passlib.context import CryptContext
from sqlalchemy.orm import relationship
from .rating import Rating

bcrypt_context = CryptContext(schemes=["bcrypt"])

class User(Base, BaseEntity):
    __tablename__ = "users"
    
    email = Column(String, unique=True)
    hashed_password = Column(String)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Time)
    photo_url = Column(String)
    telephone = Column(String)
    address = Column(String)
    experience_in = Column(String)
    addition_detail = Column(String)
    is_active = Column(Boolean, nullable=False, default = True)
    is_admin = Column(Boolean, nullable=False, default = False)
    ratings = relationship('Rating', back_populates='user', lazy='immediate')
    
    def get_id(self) -> str:
        return str(self.id)
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    
def get_hashed_password(password):
    return bcrypt_context.hash(password)

def verify_password(plain_text_pass, hashed_password):
    return bcrypt_context.verify(plain_text_pass, hashed_password)