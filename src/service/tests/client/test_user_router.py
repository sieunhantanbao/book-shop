from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from datetime import datetime
from app.main import app
from app.schemas.user import User
from app.services.auth import token_interceptor
from app.database import get_db_context
from app.models.user import UserProfileViewModel
from app.services import user as user_service
from fastapi import status, UploadFile
from io import BytesIO
from uuid import UUID

# Create a mock for the token_interceptor dependency
def override_token_interceptor():
    return User(
        id= UUID("12345678-1234-5678-1234-567812345678"),
        email="test@example.com",
        first_name="Test",
        last_name="User"
    )

# Create a mock for the get_db_context dependency
def override_get_db_context():
    # This would be a mock of your database session or context
    db_mock = MagicMock()
    return db_mock

# Apply the dependency overrides
app.dependency_overrides[token_interceptor] = override_token_interceptor
app.dependency_overrides[get_db_context] = override_get_db_context

client = TestClient(app)

# Mocking the user_service.get_user_by_id function
user_service.get_user_by_id = MagicMock(return_value=UserProfileViewModel(
    email="test@example.com",
    first_name="Test",
    last_name="User",
    telephone="123456789",
    address="123 Test St",
    experience_in="Testing",
    addition_detail="Additional details",
    date_of_birth=datetime(1990, 1, 1)
))

def test_get_my_profile():
    response = client.get("/api/users/profile")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["first_name"] == "Test"
    assert data["last_name"] == "User"
    assert data["telephone"] == "123456789"
    assert data["address"] == "123 Test St"
    assert data["experience_in"] == "Testing"
    assert data["addition_detail"] == "Additional details"
    assert data["date_of_birth"] == "1990-01-01T00:00:00"

##############################################################################################

# Mocking the user_service.create_or_update_user function
def mock_create_or_update_user(db, model):
    if model.email == "conflict@example.com":
        return status.HTTP_409_CONFLICT
    elif model.email == "error@example.com":
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    return status.HTTP_201_CREATED

user_service.create_or_update_user = MagicMock(side_effect=mock_create_or_update_user)

def test_create_user_success():
    new_user = {
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User",
        "is_active": True,
        "is_admin": False,
        "password": "Password123!@#",
        "confirm_password": "Password123!@#"
    }
    response = client.post("/api/users", json=new_user)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == True

def test_create_user_conflict():
    new_user = {
        "email": "conflict@example.com",
        "first_name": "New",
        "last_name": "User",
        "is_active": True,
        "is_admin": False,
        "password": "Password123!@#",
        "confirm_password": "Password123!@#"
    }
    response = client.post("/api/users", json=new_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "The email has already exist"}

def test_create_user_internal_error():
    new_user = {
        "email": "error@example.com",
        "first_name": "New",
        "last_name": "User",
        "is_active": True,
        "is_admin": False,
        "password": "Password123!@#",
        "confirm_password": "Password123!@#"
    }
    response = client.post("/api/users", json=new_user)
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "There was an error while creating user"}
    
##############################################################################################

# Mocking the user_service.change_password function
def mock_change_password(db, model):
    if model.new_password == "NotfoundNewPassword12!@#":
        return status.HTTP_404_NOT_FOUND
    elif model.new_password == "InternalErrorNewPassword12!@#":
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    return status.HTTP_200_OK

user_service.change_password = MagicMock(side_effect=mock_change_password)

def test_change_password_success():
    change_password_data = {
        "email": "test@example.com",
        "old_password": "Password123!@#",
        "new_password": "SuccessNewPassword12!@#",
        "confirm_new_password": "SuccessNewPassword12!@#"
    }
    response = client.post("/api/users/change-password", json=change_password_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == True

def test_change_password_unauthorized():
    change_password_data = {
        "email": "unauthorized@example.com",
        "old_password": "Password123!@#",
        "new_password": "UnauthorizedNewPassword12!@#",
        "confirm_new_password": "UnauthorizedNewPassword12!@#"
    }
    response = client.post("/api/users/change-password", json=change_password_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Your are not authorized to perform this action"}

def test_change_password_user_not_found():
    change_password_data = {
        "email": "test@example.com",
        "old_password": "Password123!@#",
        "new_password": "NotfoundNewPassword12!@#",
        "confirm_new_password": "NotfoundNewPassword12!@#"
    }
    response = client.post("/api/users/change-password", json=change_password_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User does not exist or invalid current password"}

def test_change_password_internal_error():
    change_password_data = {
        "email": "test@example.com",
        "old_password": "Password123!@#",
        "new_password": "InternalErrorNewPassword12!@#",
        "confirm_new_password": "InternalErrorNewPassword12!@#"
    }
    response = client.post("/api/users/change-password", json=change_password_data)
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "There was an error while changing the password"}
    
##############################################################################################

# Mocking the user_service.update_profile function
def mock_update_profile(db, model):
    if model.first_name == "notfound":
        return status.HTTP_404_NOT_FOUND
    elif model.first_name == "error":
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    return status.HTTP_200_OK

user_service.update_profile = MagicMock(side_effect=mock_update_profile)

def test_update_myprofile_success():
    update_profile_data = {
        "email": "test@example.com",
        "first_name": "success",
        "last_name": "User",
        "telephone": "1234567890",
        "address": "123 Test St",
        "experience_in": "Software Development",
        "addition_detail": "Some additional detail",
        "date_of_birth": "1990-01-01"
    }
    response = client.post("/api/users/profile", json=update_profile_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == True

def test_update_myprofile_unauthorized():
    update_profile_data = {
        "email": "unauthorized@example.com",
        "first_name": "unauthorized",
        "last_name": "User",
        "telephone": "1234567890",
        "address": "123 Test St",
        "experience_in": "Software Development",
        "addition_detail": "Some additional detail",
        "date_of_birth": "1990-01-01"
    }
    response = client.post("/api/users/profile", json=update_profile_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Your are not authorized to perform this action"}

def test_update_myprofile_user_not_found():
    update_profile_data = {
        "email": "test@example.com",
        "first_name": "notfound",
        "last_name": "User",
        "telephone": "1234567890",
        "address": "123 Test St",
        "experience_in": "Software Development",
        "addition_detail": "Some additional detail",
        "date_of_birth": "1990-01-01"
    }
    response = client.post("/api/users/profile", json=update_profile_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User does not exist or invalid current password"}

def test_update_myprofile_internal_error():
    update_profile_data = {
        "email": "test@example.com",
        "first_name": "error",
        "last_name": "User",
        "telephone": "1234567890",
        "address": "123 Test St",
        "experience_in": "Software Development",
        "addition_detail": "Some additional detail",
        "date_of_birth": "1990-01-01"
    }
    response = client.post("/api/users/profile", json=update_profile_data)
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "There was an error while updating the profile"}
    
#####################################################################################

# Mocking the user_service.upload_profile_photo function
def mock_upload_profile_photo(db, user_id, photo):
    if photo.filename == "notfound.png":
        return status.HTTP_404_NOT_FOUND
    elif photo.filename == "badrequest.png":
        return status.HTTP_400_BAD_REQUEST
    elif photo.filename =="internalerror.png":
        return status.HTTP_500_INTERNAL_SERVER_ERROR
    return status.HTTP_200_OK

user_service.upload_profile_photo = MagicMock(side_effect=mock_upload_profile_photo)

def test_change_profile_photo_success():
    file = BytesIO(b"fake image data")
    response = client.post("/api/users/profile/photo", params={"user_id": UUID("12345678-1234-5678-1234-567812345678")}, files={"photo": ("photo.png", file, "image/png")})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == True

def test_change_profile_photo_unauthorized():
    file = BytesIO(b"fake image data")
    response = client.post("/api/users/profile/photo", params={"user_id": UUID("52345678-1234-5678-1234-567812345678")}, files={"photo": ("photo.png", file, "image/png")})
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json() == {"detail": "Your are not authorized to perform this action"}

def test_change_profile_photo_user_not_found():
    file = BytesIO(b"fake image data")
    response = client.post("/api/users/profile/photo", params={"user_id": UUID("12345678-1234-5678-1234-567812345678")}, files={"photo": ("notfound.png", file, "image/png")})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User does not exist"}

def test_change_profile_photo_bad_request():
    file = BytesIO(b"fake image data")
    response = client.post("/api/users/profile/photo", params={"user_id": UUID("12345678-1234-5678-1234-567812345678")}, files={"photo": ("badrequest.png", file, "image/png")})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Bad request: profile photo is not provided"}

def test_change_profile_photo_internal_error():
    file = BytesIO(b"fake image data")
    response = client.post("/api/users/profile/photo", params={"user_id": UUID("12345678-1234-5678-1234-567812345678")}, files={"photo": ("internalerror.png", file, "image/png")})
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "There was an error while uploading user profile photo"}