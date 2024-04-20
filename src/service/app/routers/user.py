from fastapi import APIRouter, Depends, UploadFile, status
from services.user import UserCreateOrUpdateModel, ChangeUserPasswordModel, UpdateMyProfileModel, UserProfileViewModel
from ultils.utils import http_exception
from services.auth import token_interceptor
from database import get_db_context
from sqlalchemy.orm import Session
from uuid import UUID
from schemas.user import User
from services import user as user_service

router = APIRouter(prefix="/api/users", tags=["User"])

@router.get("/profile", status_code=status.HTTP_200_OK)
async def get_my_profile(user: User = Depends(token_interceptor),
                         db: Session = Depends(get_db_context)) -> UserProfileViewModel:
    """ Get user profile

    Args:
        user (User, optional): User from token. Defaults to Depends(token_interceptor).
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Returns:
        UserProfileViewModel: A user view model
    """
    my_profile = user_service.get_user_by_id(user.id, db)
    return my_profile

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_a_new_user(model: UserCreateOrUpdateModel, 
                            db: Session = Depends(get_db_context))->bool:
    """ Create a new user

    Args:
        model (UserCreateOrUpdateModel): user to create
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Raises:
        http_exception: 409 Conflict in case the user_name or email exist
        http_exception: 500 Internal error for the server error

    Returns:
        bool: True if sucess
    """
    result = user_service.create_or_update_user(db, model)
    match result:
        case status.HTTP_201_CREATED:
            return True
        case status.HTTP_409_CONFLICT:
            raise http_exception(409, "The email has already exist")
        case status.HTTP_500_INTERNAL_SERVER_ERROR:
            raise http_exception(500, "There was an error while creating user")

@router.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(model: ChangeUserPasswordModel,
                          user: User = Depends(token_interceptor),
                          db: Session = Depends(get_db_context)):
    """ Change password
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if user.email != model.email:
        raise http_exception(403, "Your are not authorized to perform this action")
    result = user_service.change_password(db, model)
    match result:
        case status.HTTP_200_OK:
            return True
        case status.HTTP_404_NOT_FOUND:
            raise http_exception(404, "User does not exist or invalid current password")
        case status.HTTP_500_INTERNAL_SERVER_ERROR:
            raise http_exception(500, "There was an error while creating user")
    
@router.post('/profile', status_code=status.HTTP_200_OK)
async def update_myprofile(model: UpdateMyProfileModel,
                          user: User = Depends(token_interceptor),
                          db: Session = Depends(get_db_context)):
    """ Update user profile
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    if user.email != model.email:
        raise http_exception(403, "Your are not authorized to perform this action")
    result = user_service.update_profile(db, model)
    match result:
        case status.HTTP_200_OK:
            return True
        case status.HTTP_404_NOT_FOUND:
            raise http_exception(404, "User does not exist or invalid current password")
        case status.HTTP_500_INTERNAL_SERVER_ERROR:
            raise http_exception(500, "There was an error while creating user")

@router.post('/profile/photo')
async def change_profile_photo(user_id: UUID,
                          photo: UploadFile,
                          user: User = Depends(token_interceptor),
                          db: Session = Depends(get_db_context)):
    """ Update user profile photo

    Returns:
        _type_: _description_
    """
    if user_id != user.id:
        raise http_exception(403, "Your are not authorized to perform this action")
    result = user_service.upload_profile_photo(db, user_id, photo)
    match result:
        case status.HTTP_200_OK:
            return True
        case status.HTTP_404_NOT_FOUND:
            raise http_exception(404, "User does not exist")
        case status.HTTP_400_BAD_REQUEST:
            raise http_exception(400, "Bad request: profile photo is not provided")
        case status.HTTP_500_INTERNAL_SERVER_ERROR:
            raise http_exception(500, "There was an error while uploading user profile photo")