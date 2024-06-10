from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel
from app.models.image import ImageViewModel

class BaseAdminCategoryViewModel(BaseModel):
    id: UUID
    name: str
    slug: str
    short_description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    sort_order: Optional[str] = None
    images: Optional[List[ImageViewModel]] = None
    
    class ConfigDict:
        from_attributes: True
        
class AdminCategoryCreateOrUpdateRequestModel(BaseModel):
    id: Optional[UUID] = None
    name: str
    short_description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    sort_order: Optional[int] = 0

    class ConfigDict:
        validate_assignment = True
    