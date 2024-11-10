from datetime import datetime
from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, UploadFile, status, Form
from sqlalchemy.orm import Session
from app.ultils.extensions import clear_redis_cache
from app.ultils.constants import REDIS_KEY_CLIENT_LIST_ALL_BOOKS, REDIS_KEY_CLIENT_LIST_FEATURED_BOOKS
from app.models.admin.book import AdminBookCreateOrUpdateRequestModel, BaseAdminBookViewModel
from app.ultils.utils import http_exception
from app.services.auth import admin_token_interceptor
from app.database import get_db_context
from app.schemas.user import User
from app.services.admin import book as _book_service

router = APIRouter(prefix="/api/admin/books", tags=["Administrator Book"])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all_books(db: Session = Depends(get_db_context),
                         user: User = Depends(admin_token_interceptor)) -> List[BaseAdminBookViewModel]:
    """ Get all books

    Args:
        db (Session, optional): Db Context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(admin_token_interceptor).

    Returns:
        List[BaseAdminBookViewModel]: List of books
    """
    if user:
        books = _book_service.get_all(db)
        return books
    return http_exception(401, "You are not authorized to pefrom this action")


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_a_book(
                        title: str = Form(...),
                        short_description: str = Form(None),
                        description: str = Form(None),
                        price: float = Form(...),
                        isbn: str = Form(...),
                        author: str = Form(...),
                        publisher: str = Form(None),
                        publish_date: datetime = Form(None),
                        pages: int = Form(...),
                        dimensions: str = Form(None),
                        language: str = Form(None),
                        thumbnail_url: str = Form(None),
                        sort_order: int = Form(0),
                        is_featured: bool = Form(False),
                        is_published: bool = Form(True),
                        category_id: UUID = Form(...),
                        files: List[UploadFile] = None,
                        db: Session = Depends(get_db_context),
                        user: User = Depends(admin_token_interceptor)) -> bool:
    """ Create a new book

    Args:
        title (str, optional): _description_. Defaults to Form(...).
        short_description (str, optional): _description_. Defaults to Form(None).
        description (str, optional): _description_. Defaults to Form(None).
        price (float, optional): _description_. Defaults to Form(...).
        isbn (str, optional): _description_. Defaults to Form(...).
        author (str, optional): _description_. Defaults to Form(...).
        publisher (str, optional): _description_. Defaults to Form(None).
        publish_date (datetime, optional): _description_. Defaults to Form(None).
        pages (int, optional): _description_. Defaults to Form(...).
        dimensions (str, optional): _description_. Defaults to Form(None).
        language (str, optional): _description_. Defaults to Form(None).
        thumbnail_url (str, optional): _description_. Defaults to Form(None).
        sort_order (int, optional): _description_. Defaults to Form(0).
        is_featured (bool, optional): _description_. Defaults to Form(False).
        is_published (bool, optional): _description_. Defaults to Form(True).
        category_id (UUID, optional): _description_. Defaults to Form(...).
        files (List[UploadFile], optional): _description_. Defaults to None.
        db (Session, optional): _description_. Defaults to Depends(get_db_context).
        user (User, optional): _description_. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        model = AdminBookCreateOrUpdateRequestModel(
            title=title, short_description=short_description, description=description,
            price=price, isbn=isbn, author=author, publisher=publisher,
            publish_date=publish_date, pages=pages, dimensions=dimensions,
            language=language, thumbnail_url=thumbnail_url, sort_order=sort_order,
            is_featured=is_featured, is_published=is_published, category_id=category_id
        )
        result = _book_service.create(db, model, files)
        if result:
            cache_keys = [REDIS_KEY_CLIENT_LIST_ALL_BOOKS, REDIS_KEY_CLIENT_LIST_FEATURED_BOOKS]
            clear_redis_cache(cache_keys)
            return result
        return http_exception(500, "There was an error while creating the book")
    return http_exception(401, "You are not authorized to pefrom this action")


@router.put('/edit/{book_id}', status_code=status.HTTP_200_OK)
async def edit(book_id:UUID,
            title: str = Form(...),
            short_description: str = Form(None),
            description: str = Form(None),
            price: float = Form(...),
            isbn: str = Form(...),
            author: str = Form(...),
            publisher: str = Form(None),
            publish_date: datetime = Form(None),
            pages: int = Form(...),
            dimensions: str = Form(None),
            language: str = Form(None),
            thumbnail_url: str = Form(None),
            sort_order: int = Form(0),
            is_featured: bool = Form(False),
            is_published: bool = Form(True),
            category_id: UUID = Form(...),
            files: List[UploadFile] = None, 
            db: Session = Depends(get_db_context),
            user: User = Depends(admin_token_interceptor)) -> bool:
    """ Edit a book

    Args:
        book_id (UUID): _description_
        title (str, optional): _description_. Defaults to Form(...).
        short_description (str, optional): _description_. Defaults to Form(None).
        description (str, optional): _description_. Defaults to Form(None).
        price (float, optional): _description_. Defaults to Form(...).
        isbn (str, optional): _description_. Defaults to Form(...).
        author (str, optional): _description_. Defaults to Form(...).
        publisher (str, optional): _description_. Defaults to Form(None).
        publish_date (datetime, optional): _description_. Defaults to Form(None).
        pages (int, optional): _description_. Defaults to Form(...).
        dimensions (str, optional): _description_. Defaults to Form(None).
        language (str, optional): _description_. Defaults to Form(None).
        thumbnail_url (str, optional): _description_. Defaults to Form(None).
        sort_order (int, optional): _description_. Defaults to Form(0).
        is_featured (bool, optional): _description_. Defaults to Form(False).
        is_published (bool, optional): _description_. Defaults to Form(True).
        category_id (UUID, optional): _description_. Defaults to Form(...).
        files (List[UploadFile], optional): _description_. Defaults to None.
        db (Session, optional): _description_. Defaults to Depends(get_db_context).
        user (User, optional): _description_. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: _description_
    """
    if user:
        model = AdminBookCreateOrUpdateRequestModel(
            id=book_id, title=title, short_description=short_description, description=description,
            price=price, isbn=isbn, author=author, publisher=publisher,
            publish_date=publish_date, pages=pages, dimensions=dimensions,
            language=language, thumbnail_url=thumbnail_url, sort_order=sort_order,
            is_featured=is_featured, is_published=is_published, category_id=category_id
        )
        result = _book_service.edit(db, model, files)
        if result:
            cache_keys = [REDIS_KEY_CLIENT_LIST_ALL_BOOKS, REDIS_KEY_CLIENT_LIST_FEATURED_BOOKS]
            clear_redis_cache(cache_keys)
            return result
        return http_exception(500, "There was an error while editing the book")
    return http_exception(401, "You are not authorized to pefrom this action")


@router.put('/publish/{book_id}/{action}', status_code=status.HTTP_200_OK)
async def publish(book_id: UUID, action: str, 
                db: Session = Depends(get_db_context),
                user: User = Depends(admin_token_interceptor)) -> bool:
    """ Publish a book

    Args:
        book_id (UUID): Book id
        action (str): _description_
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User form token. Defaults to Depends(admin_token_interceptor).

    Returns:
        bool: True if success else False
    """
    if user:
        result = _book_service.publish(db, book_id, action)
        if result:
            cache_keys = [REDIS_KEY_CLIENT_LIST_ALL_BOOKS, REDIS_KEY_CLIENT_LIST_FEATURED_BOOKS]
            clear_redis_cache(cache_keys)
        return http_exception(500, "There was an error while publishing the book")
    return http_exception(401, "You are not authorized to pefrom this action")

