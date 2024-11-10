
from datetime import timedelta
from typing import Optional
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db_context
from app.services import auth as auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token")
async def get_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_context)):
    """ Generate a new access token from login

    Args:
        form_data (OAuth2PasswordRequestForm, optional): _description_. Defaults to Depends().
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Raises:
        auth_service.token_exception: 401 Unauthorized

    Returns:
        _type_: Access token, Referesh token
    """
    user = auth_service.authenticate(form_data.username, form_data.password, db)
    if not user:
        raise auth_service.token_exception(status.HTTP_401_UNAUTHORIZED)
    
    return auth_service.generate_tokens(user)

@router.post("/refresh-token")
async def do_refresh_token(refresh_token: str, db: Session = Depends(get_db_context)):
    """_summary_

    Args:
        refresh_token (str): Referesh token
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Returns:
        _type_: Access token + Referesh token
    """
    user_from_token = auth_service.do_refresh_token(refresh_token)
    user = auth_service.authenticate_by_user_id(user_from_token.id, db)
    return auth_service.generate_tokens(user)