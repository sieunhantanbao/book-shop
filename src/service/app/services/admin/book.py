from datetime import datetime
from typing import List
from uuid import UUID
from fastapi import UploadFile
from sqlalchemy.orm import Session
from slugify import slugify
from ultils.extensions import allowed_file, upload_file
from models.admin.book import BaseAdminBookViewModel, AdminBookCreateOrUpdateRequestModel
from models.admin.category import BaseAdminCategoryViewModel, AdminCategoryCreateOrUpdateRequestModel
from schemas.category import Category
from schemas.book import Book
from schemas.image import Image


def get_all(db: Session) -> List[BaseAdminBookViewModel]:
    """ Get all books
    Args:
        db (Session): Db context

    Returns:
        List[BaseAdminBookViewModel]: A list of books
    """
    books = db.query(Book).all()
    return books


def create(db: Session, model: AdminBookCreateOrUpdateRequestModel, files: List[UploadFile] = None) -> bool:
    """ Create a book

    Args:
        db (Session): Db context
        model (AdminBookCreateOrUpdateRequestModel): Book create model
        images (Optional[List[UploadFile]], optional): List of images. Defaults to None.

    Returns:
        bool: True if success else False
    """
    try:
        new_book = Book(title = model.title,
                        short_description = model.short_description,
                        slug = slugify(model.title),
                        price = model.price,
                        description = model.description,
                        isbn = model.isbn,
                        author = model.author,
                        publisher = model.publisher,
                        pages = model.pages,
                        dimensions = model.dimensions,
                        language = model.language,
                        is_featured = model.is_featured,
                        is_published = model.is_published,
                        created_at = datetime.now(),
                        category_id = model.category_id
                        )
        publish_date = model.publish_date
        if publish_date is not None and publish_date !='':
            new_book.publish_date = datetime.strptime(publish_date, '%m/%d/%Y')

        for file in files:
            if file.filename != '' and allowed_file(file.filename):
                file_name = upload_file(file)
                image = Image(url = file_name)
                new_book.images.append(image)
        db.add(new_book)
        db.commit()
        return True
    except Exception:
        return False


def edit(db: Session, model: AdminBookCreateOrUpdateRequestModel, files: List[UploadFile] = None) -> bool:
    """ Edit a book

    Args:
        db (Session): Db context
        book_to_edit (Book): Book id to edit
        request (Request): Request data
    """
    book_to_edit = db.query(Book).filter_by(Book.id==model.id).first()
    if not book_to_edit:
        return False # Book to edit could not be found
    
    publish_date = model.publish_date
    if publish_date is not None and publish_date !='':
        book_to_edit.publish_date = datetime.strptime(publish_date, '%m/%d/%Y')
    
    for file in files:
        if file.filename != '' and allowed_file(file.filename):
            file_name = upload_file(file)
            image = Image(url = file_name)
            book_to_edit.images.append(image)

    book_to_edit.title = model.title
    book_to_edit.slug = slugify(book_to_edit.title)
    book_to_edit.short_description = model.short_description
    book_to_edit.price = model.price
    book_to_edit.description = model.description
    book_to_edit.isbn = model.isbn
    book_to_edit.author = model.author
    book_to_edit.publisher = model.publisher
    book_to_edit.pages = model.pages
    book_to_edit.dimensions = model.dimensions
    book_to_edit.language = model.language
    book_to_edit.is_featured = model.is_featured
    book_to_edit.updated_at = datetime.now()
    book_to_edit.category_id = model.category_id
    # Update database
    db.add(book_to_edit)
    db.commit()

def publish(db: Session, book_id: UUID, action:str) -> bool:
    """ Publish a book

    Args:
        db (Session): Db context
        book_to_publish (Book): Book to publish
        action (str): Action: publish
    """
    book_to_publish = db.query(Book).filter_by(Book.id == book_id).first()
    if not book_to_publish:
        return False
    if action.lower() == 'publish':
        book_to_publish.is_published = True
    else:
        book_to_publish.is_published = False
    book_to_publish.updated_at = datetime.now()
    # Update database
    db.add(book_to_publish)
    db.commit()

def get_all_categories(db: Session) -> List[BaseAdminCategoryViewModel]:
    """ Get all categories

    Args:
        db (Session): Db context

    Returns:
        List[BaseAdminCategoryViewModel]: List of categories view model
    """
    categories = db.query(Category).all()
    return categories

def create_category(db: Session,
                    model:AdminCategoryCreateOrUpdateRequestModel,
                    file:UploadFile = None)-> bool:
    """ Create new category

    Args:
        db (Session): _description_
        model (AdminCategoryCreateOrUpdateRequestModel): _description_
        file (UploadFile): _description_

    Returns:
        bool: _description_
    """
    try:
        new_category = Category(name = model.name,
                    short_description = model.short_description,
                    slug = slugify(model.name),
                    created_at = datetime.now())
        if file is not None and file.filename != '' and allowed_file(file.filename):
            file_name = upload_file(file)
            image = Image(url = file_name)
            new_category.images.append(image)
        db.add(new_category)
        db.commit()
        return True
    except Exception:
        return False

def edit_category(db: Session, model:AdminCategoryCreateOrUpdateRequestModel, file:UploadFile = None):
    """ Edit a category

    Args:
        db (Session): Db context
        category_to_edit (Category): Category edit data
        request (Request): Request data
    """
    category_to_edit = db.query(Category).filter_by(Category.id==model.id).first()
    if not category_to_edit:
        return False
    if file is not None and file.filename != '' and allowed_file(file.filename):
        file_name = upload_file(file)
        image = Image(url = file_name)
        category_to_edit.images.append(image)

    category_to_edit.name = model.name
    category_to_edit.slug = slugify(category_to_edit.name)
    category_to_edit.short_description = model.short_description
    category_to_edit.updated_at = datetime.now()
    # Update database
    db.add(category_to_edit)
    db.commit()