from datetime import timedelta
from datetime import datetime, timezone
import time
from typing import Optional
import jwt
from jwt import PyJWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from uuid import UUID
from schemas.user import User, verify_password
from ultils.constants import ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_MINUTES
from settings import JWT_SECRET, JWT_ALGORITHM

oa2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")
opt_oa2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token", auto_error=False)

def authenticate(email: str, password: str, db: Session):
    """ Authenticate user login

    Args:
        email (str): Email of the user
        password (str): Password
        db (Session): Db context

    Returns:
        _type_: _description_
    """
    user = db.query(User).filter(User.email == email, User.is_active).first()

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def authenticate_by_user_id(user_id: UUID, db: Session):
    """ Authenticate user by user id (refresh token)

    Args:
        user_id (UUID): User Id
        db (Session): Db context

    Returns:
        _type_: False if user does not exist else found user.
    """
    user = db.query(User).filter(User.id == user_id, User.is_active).first()

    if not user:
        return False
    return user

def token_exception(status_code) -> HTTPException:
    """ Raise token exception

    Args:
        status_code (_type_): _description_

    Returns:
        HTTPException: _description_
    """
    match status_code:
        case status.HTTP_401_UNAUTHORIZED:
            return HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Invalid username or password",
                headers = {"WWW-Authenticate": "Bearer"}
            )
        case status.HTTP_403_FORBIDDEN:
            return HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail = "Access forbidden",
                headers = {"WWW-Authenticate": "Bearer"}
            )
        
def generate_tokens(user: User):
    """ Generate acess token and refresh token

    Args:
        user (User): _description_

    Returns:
        _type_: _description_
    """
    access_token = __create_access_token(user, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    refresh_token = __create_refresh_token(user, timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES))
    return {
            "access_token":  access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
            }
    
def __create_access_token(user: User, expires: Optional[timedelta] = None):
    claims = {
        "sub": user.email,
        "id": str(user.id),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_admin": user.is_admin,
        "is_active": user.is_active
    }
    expire = datetime.now(timezone.utc) + expires if expires else datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    claims.update({"exp": expire})
    return jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM)

def __create_refresh_token(user: User, expires: Optional[timedelta] = None):
    claims = {
        "sub": user.email,
        "id": str(user.id)
    }
    expire = datetime.now(timezone.utc) + expires if expires else datetime.now(timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    claims.update({"exp": expire})
    return jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM)

def token_interceptor(token: str = Depends(oa2_bearer)) -> User:
    """ Token interceptor

    Args:
        token (str, optional): Token string. Defaults to Depends(oa2_bearer).

    Raises:
        token_exception: 401 Unauthorized

    Returns:
        User: _description_
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = User()
        user.email = payload.get("sub")
        user.id = UUID(payload.get("id"))
        user.first_name = payload.get("first_name")
        user.last_name = payload.get("last_name")
        user.is_admin = payload.get("is_admin")
        user.is_active = payload.get("is_active")
        if user.email is None or user.id is None or not user.is_active:
            raise token_exception(status.HTTP_401_UNAUTHORIZED)
        expiry_on = payload.get("exp")
        current_epoch_time = int(time.time())
        if expiry_on < current_epoch_time:
            raise token_exception(status.HTTP_401_UNAUTHORIZED)
        return user
    except PyJWTError:
        raise token_exception(status.HTTP_401_UNAUTHORIZED)
    
def admin_token_interceptor(token: str = Depends(oa2_bearer)) -> User:
    """Token interceptor for admin

    Args:
        token (str, optional): _description_. Defaults to Depends(oa2_bearer).

    Raises:
        token_exception: _description_

    Returns:
        User: _description_
    """
    user = token_interceptor(token)
    if not user.is_admin:
        raise token_exception(status.HTTP_403_FORBIDDEN)
    return user
    
def optional_token_interceptor(token: Optional[str] = Depends(opt_oa2_bearer)) -> Optional[User]:
    """ Optional token interceptor
    
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    try:
        if token is None:
            return None
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = User()
        user.email = payload.get("sub")
        user.id = UUID(payload.get("id"))
        user.first_name = payload.get("first_name")
        user.last_name = payload.get("last_name")
        user.is_admin = payload.get("is_admin")
        user.is_active = payload.get("is_active")
        if user.email is None or user.id is None or not user.is_active:
            return None
        return user
    except PyJWTError:
        return None
    
def do_refresh_token(token: str) -> User:
    """ Get user from the refresh token

    Args:
        token (str): Refresh token

    Raises:
        token_exception: 401 Unauthorized

    Returns:
        User: user object
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = User()
        user.email = payload.get("sub")
        user.id = UUID(payload.get("id"))
        if user.email is None or user.id is None:
            raise token_exception(status.HTTP_401_UNAUTHORIZED)
        return user
    except PyJWTError:
        raise token_exception(status.HTTP_401_UNAUTHORIZED)