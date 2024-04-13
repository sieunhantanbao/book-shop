# from uuid import UUID
# from sqlalchemy import func, desc
# from sqlalchemy.orm import Session
# from ..schemas.rating import Rating

# def get_all(db: Session, user_id: UUID) -> list[Rating]:
#     """ Get all book rating value by user_id

#     Args:
#         db (Session): Db context
#         user_id (UUID): User Id

#     Returns:
#         list[Rating]: List of Rating
#     """
#     ratings = db.query(Rating).filter(Rating.user_id==user_id, Rating.is_reviewed==True).all()
#     return ratings

# def get_rating_value_by_book_user(db: Session, user_id: UUID, book_id: UUID) -> Rating:
#     """ Get Rating value for a book by user_id

#     Args:
#         db (Session): Db Context
#         user_id (UUID): User Id
#         book_id (UUID): Book Id

#     Returns:
#         Rating: Rating object
#     """
#     return db.query(Rating).filter(Rating.user_id==user_id, Rating.book_id==book_id, Rating.is_reviewed==True).first()

# def get_all_average_rating(db: Session, book_ids:list):
#     """ Get average book ratings

#     Args:
#         db (Session): Db Context
#         book_ids (list): List of book ids

#     Returns:
#         _type_: _description_
#     """
#     average_ratings = db.query(Rating.book_id, func.avg(Rating.rating_value).label('average_rating_value'), func.count(Rating.book_id).label('total_ratings')).group_by(Rating.book_id).filter(Rating.book_id.in_(book_ids), Rating.is_reviewed).all()
#     return average_ratings

# def get_average_rating_value_by_book(db: Session, book_id: UUID):
#     """ Get average rating for a Book

#     Args:
#         db (Session): Db Context
#         book_id (UUID): Book Id

#     Returns:
#         _type_: _description_
#     """
#     return db.query(func.avg(Rating.rating_value).label('average_rating_value'), func.count(Rating.book_id).label('total_ratings')).group_by(Rating.book_id).filter_by(book_id=book_id, is_reviewed=True).all()

# def get_average_rating_statistic_by_book(db: Session, book_id: UUID):
#     """ Get average rating statistic for a Book

#     Args:
#         db (Session): Db context
#         book_id (UUID): Book Id

#     Returns:
#         _type_: _description_
#     """
#     try:
#         data = db.query(Rating.rating_value, func.count(Rating.user_id).label('total_ratings')).group_by(Rating.rating_value).filter_by(book_id=book_id, is_reviewed=True).all()
#         return True, data
#     except Exception as e:
#         print(e)
#         return False, None

# def get_book_comments(db: Session, book_id: UUID):
#     """ Get book comments

#     Args:
#         db (Session): Db context
#         book_id (UUID): Book id

#     Returns:
#         _type_: _description_
#     """
    
#     book_comments = db.query(Rating).filter_by(book_id=book_id, is_reviewed=True).order_by(desc(Rating.created_at)).all()
#     return book_comments

# def create_or_update(db: Session, user_id: UUID, book_id: UUID, rating_value: float, review_comment: str):
#     """ Add a Book rating

#     Args:
#         db (Session): Db context
#         user_id (UUID): User Id
#         book_id (UUID): Book id
#         rating_value (float): Rating value
#         review_comment (str): Review comment

#     Returns:
#         _type_: _description_
#     """
#     try:
#         new_rating = Rating(user_id=user_id,
#                             book_id=book_id,
#                             rating_value=rating_value,
#                             comment = review_comment,
#                             is_reviewed = False)
        
#         db.add(new_rating)
#         db.commit()
#         return True
#     except Exception as e:
#         print(e)
#         return False