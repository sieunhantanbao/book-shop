
from typing import List
from uuid import UUID
from sqlalchemy import desc
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.admin.rating import BaseAdminRatingViewModel
from app.schemas.rating import Rating

def get_all_pending_approval(db: Session) -> List[BaseAdminRatingViewModel]:
    """ Get all pending rating for approval

    Args:
        db (Session): _description_

    Returns:
        List[BaseAdminRatingViewModel]: List of pending rating
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
    rating_to_approve = db.query(Rating).filter_by(Rating.id==rating_id, Rating.is_reviewed==False).first()
    if rating_to_approve:
        rating_to_approve.is_reviewed = True
        rating_to_approve.updated_at = datetime.now()
        db.add(rating_to_approve)
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
    except Exception:
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
    except Exception:
        return False
