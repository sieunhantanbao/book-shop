from sqlalchemy.orm import Session
from sqlalchemy import or_
from uuid import UUID
from ultils.extensions import allowed_file, upload_file
from schemas.user import User, get_hashed_password, verify_password
from models.user import ChangeUserPasswordModel, UpdateMyProfileModel, UserCreateOrUpdateModel, UserProfileViewModel
from datetime import datetime
from fastapi import UploadFile, status
import logging

def get_user_by_id(id:UUID, db:Session) -> UserProfileViewModel:
    """ Get a user by Id
    
    Args:
        id (UUID): User Id to get
        db (Session): Db context

    Returns:
        UserViewModel: A single user object to return
    """
    return db.query(User).filter(User.id==id, User.is_active == True).first()

def create_or_update_user(db: Session, model: UserCreateOrUpdateModel, id: UUID = None) -> status:
    """ Create or update user

    Args:
        db (Session): Db context
        model (UserCreateOrUpdateModel): User model to create or update
        id (UUID, optional): Id of the user id to update. Defaults to None.

    Returns:
        status: Http Status code
    """
    try:
        if id is None: # Create new
            # To resolve the issue: 'password' is an invalid keyword argument for User
            password = model.password
            user_model = model.model_dump()
            del user_model['password']
            del user_model['confirm_password']
            # Check if the email AND/OR username exist in database
            user_exist = db.query(User).filter(User.email==model.email).first()
            if user_exist:
                logging.error("The email has been existed")
                return status.HTTP_409_CONFLICT
            new_user = User(**user_model)
            new_user.hashed_password = get_hashed_password(password)
            
            db.add(new_user)
            db.commit()
            return status.HTTP_201_CREATED
        else: # Update
            existing_user = db.query(User).filter(User.id==id).first()
            if not existing_user:
                return status.HTTP_404_NOT_FOUND
            # Check if the email AND/OR username exist in database
            if existing_user.email != model.email:
                user_exist = db.query(User).filter(User.email==model.email).first()
                if user_exist:
                    logging.error("The email=%s exists", model.email)
                    return status.HTTP_409_CONFLICT
            existing_user.first_name = model.first_name
            existing_user.last_name = model.last_name
            existing_user.email = model.email
            existing_user.is_active = model.is_active
            existing_user.is_admin= model.is_admin
            existing_user.updated_at = datetime.now()
            
            db.add(existing_user)
            db.commit()
            return status.HTTP_200_OK
    except Exception as e:
        logging.error("There is an error while creating or update user. %s", e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR

def change_password(db: Session, model: ChangeUserPasswordModel) -> status:
    """ Change user password

    Args:
        db (Session): Db context
        model (ChangeUserPasswordModel): Change User password model

    Returns:
        status: Http Status code
    """
    try:
        
        existing_user = db.query(User).filter(User.email==model.email).first()
        if not verify_password(model.old_password, existing_user.hashed_password):
            return status.HTTP_404_NOT_FOUND       
        existing_user.hashed_password = get_hashed_password(model.new_password)
        existing_user.updated_at = datetime.now()
        
        db.add(existing_user)
        db.commit()
        return status.HTTP_200_OK
    except Exception as e:
        logging.error("There is an error while changing password. %s", e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR

def update_profile(db: Session, model: UpdateMyProfileModel) -> status:
    """ Update my profile

    Args:
        db (Session): Db context
        model (UpdateMyProfileModel): Update my profile model

    Returns:
        status: Status code
    """
    try:
        existing_user = db.query(User).filter(User.email==model.email).first()
        if not existing_user:
            return status.HTTP_404_NOT_FOUND
        existing_user.first_name = model.first_name
        existing_user.last_name = model.last_name
        existing_user.telephone = model.telephone
        existing_user.address = model.address
        existing_user.experience_in = model.experience_in
        existing_user.addition_detail = model.addition_detail
        existing_user.date_of_birth =  datetime.strptime(model.date_of_birth, '%m/%d/%Y')
        
        existing_user.updated_at = datetime.now()
        
        db.add(existing_user)
        db.commit()
        return status.HTTP_200_OK
    except Exception as e:
        logging.error("There is an error while updating profile. %s", e)
        return status.HTTP_500_INTERNAL_SERVER_ERROR


def upload_profile_photo(db: Session, user_id: UUID, uploaded_file: UploadFile) -> status:
    """ Upload user profile photo

    Args:
        db (Session): Db Context
        user_id (UUID): User Id
        uploaded_file (UploadFile): File upload

    Returns:
        status: Return status
    """
    if uploaded_file:
        if uploaded_file.filename != '' and allowed_file(uploaded_file.filename):
            file_name = upload_file(uploaded_file)
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                user.photo_url = file_name
                db.commit()
                return status.HTTP_200_OK
            return status.HTTP_404_NOT_FOUND
        return status.HTTP_400_BAD_REQUEST
    return status.HTTP_400_BAD_REQUEST
    


# def delete_a_user(id: UUID, db: Session) -> status:
#     """ Soft delete a user by set the is_active = False

#     Args:
#         id (UUID): Id of the user to delete
#         db (Session): Db context

#     Returns:
#         status: 404 Not found/ 204 No content
#     """
#     user_to_delete = db.query(User).filter(User.id==id).first()
#     if not user_to_delete:
#         logging.error("The user does not exist to delete")
#         return status.HTTP_404_NOT_FOUND
#     user_to_delete.is_active = False
#     db.add(user_to_delete)
#     db.commit()
#     return status.HTTP_204_NO_CONTENT
        