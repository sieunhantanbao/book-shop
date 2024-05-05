from datetime import timedelta
from datetime import datetime
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from schemas.user import User, verify_password
from jose import JWTError, jwt
from uuid import UUID
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

def create_access_token(user: User, expires: Optional[timedelta] = None):
    claims = {
        "sub": user.email,
        "id": str(user.id),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_admin": user.is_admin,
        "is_active": user.is_active
    }
    expire = datetime.now() + expires if expires else datetime.now() + timedelta(minutes=10)
    claims.update({"exp": expire})
    return jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM), expire
    
def token_interceptor(token: str = Depends(oa2_bearer)) -> User:
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
        return user
    except JWTError:
        raise token_exception(status.HTTP_401_UNAUTHORIZED)
    
def admin_token_interceptor(token: str = Depends(oa2_bearer)) -> User:
    user = token_interceptor(token)
    if not user.is_admin:
        raise token_exception(status.HTTP_403_FORBIDDEN)
    return user
    
def optional_token_interceptor(token: Optional[str] = Depends(opt_oa2_bearer)) -> Optional[User]:
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
    except JWTError:
        return None