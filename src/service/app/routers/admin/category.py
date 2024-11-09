from datetime import datetime
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, UploadFile, status, Form
from sqlalchemy.orm import Session
from app.ultils.extensions import clear_redis_cache, remove_file
from app.ultils.constants import REDIS_KEY_CLIENT_LIST_ALL_CATEGORIES, REDIS_KEY_CLIENT_LIST_SHORT_CATEGORIES
from app.models.admin.category import AdminCategoryCreateOrUpdateRequestModel, BaseAdminCategoryViewModel
from app.ultils.utils import http_exception
from app.services.auth import admin_token_interceptor
from app.database import get_db_context
from app.schemas.user import User
from app.services.admin import book as _book_service, image as _image_service

router = APIRouter(prefix="/api/admin/categories", tags=["Administrator Category"])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db_context), 
               user: User = Depends(admin_token_interceptor)) -> List[BaseAdminCategoryViewModel]:
    """ Get all categories

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        List[BaseAdminCategoryViewModel]: List of categories
    """
    if user:
        categories = _book_service.get_all_categories(db)
        return categories
    return http_exception(401, "You are not authorized to pefrom this action")


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create(
                name: str = Form(...),
                short_description: str = Form(None),
                file: UploadFile = None,
                db: Session = Depends(get_db_context), 
                user: User = Depends(admin_token_interceptor)) -> bool:
    """ Create new category

    Args:
        name (str, optional): _description_. Defaults to Form(...).
        short_description (str, optional): _description_. Defaults to Form(None).
        file (UploadFile, optional): _description_. Defaults to None.
        db (Session, optional): _description_. Defaults to Depends(get_db_context).
        user (User, optional): _description_. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        model = AdminCategoryCreateOrUpdateRequestModel(name=name, short_description=short_description)
        result = _book_service.create_category(db, model, file)
        if result:
            cache_keys = [REDIS_KEY_CLIENT_LIST_SHORT_CATEGORIES, REDIS_KEY_CLIENT_LIST_ALL_CATEGORIES]
            clear_redis_cache(cache_keys)
            return result
        return http_exception(500, "There was an error while creating the Category")
    return http_exception(401, "You are not authorized to pefrom this action")


@router.post('/edit/{cat_id}', status_code=status.HTTP_200_OK)
async def edit_category(cat_id: UUID,
                        name: str = Form(...),
                        short_description: str = Form(None),
                        file: UploadFile = None,
                        db: Session = Depends(get_db_context), 
                        user: User = Depends(admin_token_interceptor)):
    """ Edit a category

    Args:
        cat_id (UUID): _description_
        name (str, optional): _description_. Defaults to Form(...).
        short_description (str, optional): _description_. Defaults to Form(None).
        file (UploadFile, optional): _description_. Defaults to None.
        db (Session, optional): _description_. Defaults to Depends(get_db_context).
        user (User, optional): _description_. Defaults to Depends(admin_token_interceptor).

    Returns:
        _type_: _description_
    """
    if user:
        model = AdminCategoryCreateOrUpdateRequestModel(
            id=cat_id,
            name=name, short_description=short_description)
        result = _book_service.edit_category(db, model, file)
        if result:
            cache_keys = [REDIS_KEY_CLIENT_LIST_SHORT_CATEGORIES, REDIS_KEY_CLIENT_LIST_ALL_CATEGORIES]
            clear_redis_cache(cache_keys)
            return result
        return http_exception(500, "There was an error while editing the Category")
    return http_exception(401, "You are not authorized to pefrom this action")



@router.delete('/api/image/remove/{image_id}', status_code=status.HTTP_200_OK)
async def delete_image(image_id: UUID,
                       db: Session = Depends(get_db_context),
                       user: User = Depends(admin_token_interceptor))-> bool:
    """ Delete image by Id

    Args:
        image_id (UUID): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db_context).
        user (User, optional): _description_. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        result, file_name = _image_service.delete(db, image_id)
        if result:
            # Remove the physical file
            remove_file(file_name)
            return result
        return http_exception(500, "There was an error while deleting the Image")
    return http_exception(401, "You don't have permission to do this action")
