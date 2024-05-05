from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ValidationInfo, field_validator
import re

class UserProfileViewModel(BaseModel):
    email: str
    first_name: str
    last_name: str
    telephone: Optional[str] = None
    address: Optional[str] = None
    experience_in: Optional[str] = None
    addition_detail: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    class Config:
        orm_mode: True

class ChangeUserPasswordModel(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    old_password: str = Field(..., description="User's Old password")
    new_password: str = Field(..., description="User's New password")
    @field_validator('new_password')
    def validate_new_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%&*]', v):
            raise ValueError('Password must contain at least one special character (!@#$%&*)')
        return v

    @field_validator('confirm_new_password')
    def passwords_match(cls, v: str, info: ValidationInfo) -> str:
        if "new_password" in info.data and v != info.data["new_password"]:
            raise ValueError("passwords do not match")
        return v

    confirm_new_password: str
    class Config:
        validate_default = True
    

class UserCreateOrUpdateModel(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    is_active: bool = Field(default=False, description="Whether the user is active or not")
    is_admin: bool = Field(default=False, description="Whether the user is an admin or not")
    password: str = Field(..., description="User's password")

    @field_validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'[0-9]', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[!@#$%&*]', v):
            raise ValueError('Password must contain at least one special character (!@#$%&*)')
        return v
    @field_validator('confirm_password')
    def passwords_match(cls, v: str, info: ValidationInfo) -> str:
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("passwords do not match")
        return v
    confirm_password: str
    class Config:
        # Pydantic V2 config to raise all validation errors at once
        validate_default = True

class UpdateMyProfileModel(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    telephone: str = Field(..., description="User's telephone number")
    address: str = Field(..., description="User's address")
    experience_in: str = Field(..., description="User's experience in")
    addition_detail: str = Field(..., description="User's addition detail")
    date_of_birth: str = Field(..., description="User's Date of birth")
    class Config:
        # Pydantic V2 config to raise all validation errors at once
        validate_default = True
        
class AdminUserViewModel(BaseModel):
    email: str
    first_name: str
    last_name: str
    telephone: Optional[str] = None
    address: Optional[str] = None
    experience_in: Optional[str] = None
    addition_detail: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    class Config:
        orm_mode: True