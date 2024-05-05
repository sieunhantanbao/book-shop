from uuid import UUID

from models.wishlist import WishlistViewModel
from schemas.wishlist import WishList
from sqlalchemy.orm import Session

def get_all(db: Session, user_id: UUID) -> list[WishlistViewModel]:
    """ Get all wishlist by user id

    Args:
        db (Session): _description_
        user_id (UUID): User id

    Returns:
        list[WishlistViewModel]: List of book wishlist
    """
    wishlists = db.query(WishList).filter(WishList.user_id==user_id).all()
    return wishlists

def get_by_user_and_book(db: Session, user_id: UUID, book_id: UUID) -> WishList:
    """ Get wishlist by user and book id

    Args:
        db (Session): _description_
        user_id (UUID): User id
        book_id (UUID): Book id

    Returns:
        WishList: A wishlist
    """
    return db.query(WishList).filter(WishList.user_id==user_id, WishList.book_id==book_id).first()

def create(db: Session, user_id: UUID, book_id: UUID) -> bool:
    """ Create a new wishlist

    Args:
        db (Session): Db Context
        user_id (UUID): User Id
        book_id (UUID): Book Id

    Returns:
        bool: True if success else False
    """
    try:
        existing_wishlist = get_by_user_and_book(db, user_id, book_id)
        if not existing_wishlist:
            wishlist = WishList(user_id = user_id,
                        book_id = book_id
                        )
            db.add(wishlist)
            db.commit()
        return True
    except:
        return False

def delete_by_user_and_book(db: Session, user_id:UUID, book_id:UUID) -> bool:
    """ Delete a book from the wishlist

    Args:
        db (Session): Db context
        user_id (UUID): User Id
        book_id (UUID): Book Id

    Returns:
        bool: True if success else False
    """
    try:
        db.query(WishList).filter(WishList.user_id == user_id, WishList.book_id == book_id).delete()
        # Update database
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False