from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from models.admin.rating import BaseAdminRatingViewModel
from ultils.utils import http_exception
from services.auth import admin_token_interceptor
from database import get_db_context
from schemas.user import User
from services.admin import rating as _rating_service

router = APIRouter(prefix="/api/admin/ratings", tags=["Administrator Rating"])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db_context),
                  user: User = Depends(admin_token_interceptor)) -> List[BaseAdminRatingViewModel]:
    """ Get all pending rating that waiting for approval

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        List[BaseAdminRatingViewModel]: List of ratings
    """
    if user:
        rating_reviews = _rating_service.get_all_pending_approval(db)
        return rating_reviews
    return http_exception(401, "You don't have permission to do this action")

@router.post('/approve/{rating_id}', status_code=status.HTTP_200_OK)
async def approve(rating_id: UUID,
                  db: Session = Depends(get_db_context),
                  user: User = Depends(admin_token_interceptor)) -> bool:
    """ Approve an rating

    Args:
        rating_id (UUID): Rating id to approve
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        result = _rating_service.approve(db, rating_id)
        return result
    return http_exception(401, "You don't have permission to do this action")

@router.post('/delete/{rating_id}', status_code=status.HTTP_200_OK)
async def delete(rating_id: UUID,
                 db: Session = Depends(get_db_context),
                 user: User = Depends(admin_token_interceptor)) -> bool:
    """ Delete a rating

    Args:
        rating_id (UUID): Rating id to delete
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if sucess else False
    """
    if user:
        result = _rating_service.delete(db, rating_id)
        return result
    return http_exception(401, "You don't have permission to do this action")

@router.post('/approve-all/', status_code=status.HTTP_200_OK)
async def approve_all(db: Session = Depends(get_db_context),
                      user: User = Depends(admin_token_interceptor)) -> bool:
    """ Approve all pending ratings

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        result = _rating_service.approve_all(db)
        return result
    return http_exception(401, "You don't have permission to do this action")