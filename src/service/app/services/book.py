from uuid import UUID
from sqlalchemy import asc, desc, or_
from typing import List
from sqlalchemy.orm import Session
from app.models.category import CategoryForDdlViewModel, CategoryView2Model, CategoryViewModel
from app.models.book import BookDetailViewModel, BookFeaturedViewModel, BookFilterInputModel, BookRelatedViewModel
from app.schemas.book_relation import BookRelation
from app.ultils.extensions import is_valid_uuid
from app.schemas.book import Book
from app.schemas.category import Category
from app.schemas.wishlist import WishList


def get_by_id(db: Session, id_or_slug) -> BookDetailViewModel:
    """ Get book by Id

    Args:
        db (Session): Db context
        id_or_slug (_type_): Id or slug

    Returns:
        Book: A book object
    """
    is_id = UUID(id_or_slug) if is_valid_uuid(id_or_slug) else False
    if is_id is not False:
        return db.query(Book).filter(Book.id == is_id, Book.is_published).first()
    else:
        return db.query(Book).filter(Book.slug == id_or_slug, Book.is_published).first()

def get_all(db: Session, filter_model: BookFilterInputModel) -> list[BookDetailViewModel]:
    """ Get a list of book with filtering and ordering

    Args:
        db (Session): Db context
        filter (BookFilterInputModel): Filtering object

    Returns:
        list[Book]: A list of matched books
    """
    query = db.query(Book).filter(Book.is_published)
    # Filter by price
    query =  query.filter(Book.price >= filter_model.min_price_input, Book.price <= filter_model.max_price_input)
    # Filter by Keyword
    if filter_model.keyword is not None and filter_model.keyword != '':
        query = query.filter(Book.title.ilike(f"%{filter_model.keyword}%"))
    if filter_model.category_ids is not None and len(filter_model.category_ids) > 0:
        query = query.filter(or_(Book.category_id.in_(filter_model.category_ids)))
    # Order by    
    order_by = desc(Book.created_at)
    match filter_model.sort_by:
        case 'price_high_low':
            order_by = desc(Book.price)
        case 'price_low_high':
            order_by = asc(Book.price)
        case 'featured':
            order_by = desc(Book.is_featured)
    
    query = query.order_by(order_by)
    # Return data
    return query.all()

# def get_with_limit(db: Session, size: int) -> list[Book]:
#     """ Get a list of book with a size limit

#     Args:
#         db (Session): Db context
#         size (int): Number of first books to get

#     Returns:
#         list[Book]: A list of books
#     """
#     books = db.query(Book).filter(Book.is_published==True).order_by(desc(Book.created_at)).limit(size).all()
#     return books

def get_books_by_cat(
    db: Session, 
    cat_id: UUID,
    size: int = 0,
    excluded_id: UUID = None) -> list[BookRelatedViewModel]:
    """ Get books by category

    Args:
        db (Session): Db context
        cat_id (UUID): Book category Id
        size (int, optional): Number of books to get. Defaults to 0.
        excluded_id (UUID, optional): Book Id to exclude from the result. Defaults to None.

    Returns:
        list[BookRelatedViewModel]: List of books
    """
    query = db.query(Book).filter(Book.is_published==True, Book.category_id==cat_id)
    if excluded_id is not None:
        query = query.filter(Book.id != excluded_id)
    if size != 0:
        return query.limit(size).all()
    return query.all()

def get_all_categories(db: Session, size: int = 0) -> list[CategoryView2Model]:
    """ Get all categoryies

    Args:
        db (Session): Db context
        size (int, optional): Number of first categories to get. Defaults to 0.

    Returns:
        list[CategoryView2Model]: List of categories
    """
    if size and size > 0:
        return list[CategoryView2Model](db.query(Category).limit(size).all())
    else:
        return list[CategoryView2Model](db.query(Category).all())

def get_all_categories_for_ddl(db: Session) -> List[CategoryForDdlViewModel]:
    """ Get all categories for ddl

    Args:
        db (Session): Db context

    Returns:
        List[CategoryForDdlViewModel]: List of category for Drop down list
    """
    return db.query(Category).order_by(Category.name).all()
    
def get_category_by_id(db: Session, id_or_slug) -> CategoryViewModel:
    """ Get category by Id

    Args:
        db (Session): Db context
        id_or_slug (_type_): Id or slug

    Returns:
        CategoryViewModel: Category view model
    """
    is_id = int(id_or_slug) if is_valid_uuid(id_or_slug) else False
    if is_id is not False:
        return db.query(Category).filter_by(id = is_id).first()
    else:
        return db.query(Category).filter_by(slug = id_or_slug).first()

    
def get_book_wishlists(db: Session, user_id: UUID) -> List[BookRelatedViewModel]:
    """ Get all book wishlists

    Args:
        db (Session): Db context
        user_id (UUID): User Id

    Returns:
        List[BookRelatedViewModel]: List of book related view model
    """
    return db.query(Book).join(WishList).filter(WishList.user_id==user_id, Book.id==WishList.book_id).all()

def get_featured(db: Session, size: int) -> List[BookFeaturedViewModel]:
    """ Get featured books

    Args:
        db (Session): Db context
        size (int): Maximum number of items to return

    Returns:
        List[BookFeaturedViewModel]: List of books
    """
    books = db.query(Book).filter(Book.is_published, Book.is_featured).order_by(desc(Book.created_at)).limit(size).all()
    return books

def get_related_books(db: Session, book_id: UUID) -> list[BookRelatedViewModel]:
    """ Get books related

    Args:
        db (Session): Db context
        book_id (UUID): Book Id

    Returns:
        list[BookRelatedViewModel]: List of related books
    """
    related_books = (
        db.query(Book)
        .join(
            BookRelation,
            or_(
                Book.id == BookRelation.book_id_1,
                Book.id == BookRelation.book_id_2
            )
        )
        .filter(
            or_(
                BookRelation.book_id_1 == book_id,
                BookRelation.book_id_2 == book_id
            ),
            Book.id != book_id
        )
        .all()
    )
    return related_books
