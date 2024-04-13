
from uuid import UUID
from sqlalchemy import desc
from ..schemas.rating import Rating
from datetime import datetime
from sqlalchemy.orm import Session

def get_all(db: Session):
    """ Get all ratings and reviews

    Args:
        db (Session): Db context

    Returns:
        _type_: _description_
    """
    rating_reviews = db.query(Rating).query.order_by(desc(Rating.created_at)).all()
    return rating_reviews

def get_all_pending_approval(db: Session) -> list[Rating]:
    """ Get all pending Ratings

    Args:
        db (Session): Db context

    Returns:
        list[Rating]: A list of pending Ratings
    """
    rating_reviews = db.query(Rating).filter(Rating.is_reviewed==False).order_by(desc(Rating.created_at)).all()
    return rating_reviews

def approve(db: Session, rating_id: UUID) -> bool:
    """ Apporve a book rating

    Args:
        db (Session): Db context
        rating_id (UUID): Rating id

    Returns:
        bool: True if success else False
    """
    rating_to_approve = db.query(Rating).filter_by(id=rating_id, is_reviewed =False).first()
    if rating_to_approve:
        rating_to_approve.is_reviewed = True
        rating_to_approve.updated_at = datetime.now()
        db.commit()
        return True
    return False

def approve_all(db: Session) -> bool:
    """ Approve all pending Ratings

    Args:
        db (Session): Db context

    Returns:
        bool: True if success else False
    """
    try:
        ratings_to_approve = db.query(Rating).filter(Rating.is_reviewed == False).all()
        for rating_to_approve in ratings_to_approve:
            rating_to_approve.is_reviewed = True
            rating_to_approve.updated_at = datetime.now()
        db.commit()
        return True
    except:
        return False

def delete(db: Session, rating_id: UUID) -> bool:
    """ Delete a rating

    Args:
        db (Session): Db context
        rating_id (UUID): Rating id

    Returns:
        bool: True if success else False
    """
    try:
        rating_to_delete = db.query(Rating).filter(Rating.id == rating_id).first()
        if rating_to_delete:
            db.delete(rating_to_delete)
            db.commit()
            return True
        else:
            return False
    except:
        return False
