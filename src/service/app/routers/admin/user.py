from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.models.user import AdminUserViewModel
from app.ultils.utils import http_exception
from app.services.auth import admin_token_interceptor
from app.database import get_db_context
from app.schemas.user import User
from app.services import user as _user_service

router = APIRouter(prefix="/api/admin/users", tags=["Administrator User"])

@router.get('/', status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db_context),
            user: User = Depends(admin_token_interceptor)) -> List[AdminUserViewModel]:
    """ Get list of users for admin

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        List[AdminUserViewModel]: List of users
    """
    if user:
        users = _user_service.get_all(db)
        return users
    return http_exception(401, "You don't have permission to do this action")

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create(db: Session = Depends(get_db_context),
                 user: User = Depends(admin_token_interceptor)) -> bool:
    """ [NOT COMPLETED YET] Create a new user from admin

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        # result = _user_service
        result = True
        return result
    return http_exception(401, "You don't have permission to do this action")
