import json
from typing import List, Optional, Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from models.rating import BookReviewCreateModel
from models.category import CategoryDetailViewModel, CategoryView2Model, CategoryViewModel
from ultils import constants
from ultils.utils import http_exception
from services.auth import token_interceptor
from database import get_db_context, redis_client
from schemas.user import User
from services import book as book_service, rating as rating_service, wishlist as wishlist_service
from models.book import BookDetailViewModel, BookFeaturedViewModel, BookFilterInputModel, BookRelatedViewModel

router = APIRouter(prefix="/api/books", tags=["Book"])

@router.get("/wishlist", status_code = status.HTTP_200_OK)
async def get_book_wishlist(db: Session = Depends(get_db_context),
                         user: User = Depends(token_interceptor)) -> List[BookRelatedViewModel]:
    """ Get list of book wishlist

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from JWT Token. Defaults to Depends(token_interceptor).

    Returns:
        List[BookDetailViewModel]: List of Book view model
    """
    books = book_service.get_book_wishlists(db, user.id)
    __build_book_ratings(db, books)
    return books

@router.get('/categories', status_code=status.HTTP_200_OK)
async def get_categories(get_all: bool = True,
                    db: Session = Depends(get_db_context))-> List[CategoryView2Model]:
    """ Get all categories

    Args:
        get_all (bool, optional): get_all flag. Defaults to True.
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Returns:
        List[CategoryView2Model]: Return data type
    """
    if not get_all:
        # Get first 6 categories
        serialized_categories_cached = redis_client.get(constants.REDIS_KEY_CLIENT_LIST_SHORT_CATEGORIES)
        if serialized_categories_cached is None:
            categories = book_service.get_all_categories(db, constants.NUMBER_OF_CATEGORIES_ON_HOME_PAGE)
            for category in categories:
                if category.images and category.images[0] is not None:
                    category.thumbnail_url = category.images[0].url
                else:
                    category.thumbnail_url = None
            categories_dic = [category.as_dict() for category in categories]
            serialized_categories_list = json.dumps(categories_dic)
            redis_client.set(constants.REDIS_KEY_CLIENT_LIST_SHORT_CATEGORIES, serialized_categories_list)
            serialized_categories_cached = serialized_categories_list
    else:
        # Get full categories
        serialized_categories_cached = redis_client.get(constants.REDIS_KEY_CLIENT_LIST_ALL_CATEGORIES)
        if serialized_categories_cached is None:
            categories = book_service.get_all_categories(db)
            for category in categories:
                if category.images and category.images[0] is not None:
                    category.thumbnail_url = category.images[0].url
                else:
                    category.thumbnail_url = None
            categories_dic = [category.as_dict() for category in categories]
            serialized_categories_list = json.dumps(categories_dic)
            redis_client.set(constants.REDIS_KEY_CLIENT_LIST_ALL_CATEGORIES, serialized_categories_list)
            serialized_categories_cached = serialized_categories_list
    return json.loads(serialized_categories_cached)


@router.get('/featured-books', status_code=status.HTTP_200_OK)
async def get_featured_books(db: Session = Depends(get_db_context))-> List[BookFeaturedViewModel]:
    """API Get 10 latest featured books with Redis cache

    Args:
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Returns:
        List[BookFeaturedViewModel]: List of featured books model
    """
    serialized_featured_books_cached = redis_client.get(constants.REDIS_KEY_CLIENT_LIST_FEATURED_BOOKS)
    if serialized_featured_books_cached is None:
        featured_books = book_service.get_featured(db, constants.NUMBER_OF_FEATURED_CAROUSEL)
        for featured_book in featured_books:
            featured_book.thumbnail_url = featured_book.images[0].url if featured_book.images[0] is not None else None
        featured_books_dict = [featured_book.as_dict() for featured_book in featured_books]
        serialized_featured_books_list = json.dumps(featured_books_dict)
        redis_client.set(constants.REDIS_KEY_CLIENT_LIST_FEATURED_BOOKS, serialized_featured_books_list)
        serialized_featured_books_cached = serialized_featured_books_list
    return json.loads(serialized_featured_books_cached)

@router.get('/search')
async def book_list(min_price_input: float,
                    max_price_input: float,
                    min_rate_input: int,
                    max_rate_input: int,
                    sort_by: Optional[str] = None,
                    keyword: Optional[str] = None,
                    category: Annotated[list[UUID] | None, Query()] = None,
                    db: Session = Depends(get_db_context))-> List[BookDetailViewModel]:
    """ Get all books with filtering

    Args:
        min_price_input (float): Min price input
        max_price_input (float): Max price input
        min_rate_input (int): Min rate input (0-5)
        max_rate_input (int): Max rate input (0-5)
        sort_by (Optional[str], optional): Sort by. Defaults to None.
        keyword (Optional[str], optional): Keyword search. Defaults to None.
        category (Annotated[list[UUID]  |  None, Query, optional): List of categoryId. Defaults to None.
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Returns:
        List[BookDetailViewModel]: List of book detail view model
    """
    filter_model = BookFilterInputModel(keyword = keyword,
                                        min_price_input = min_price_input,
                                        max_price_input = max_price_input,
                                        min_rate_input = min_rate_input,
                                        max_rate_input = max_rate_input,
                                        category = category,
                                        sort_by = sort_by)
    books = book_service.get_all(db, filter_model)
    __build_book_ratings(db, books)
    # Filter by rating
    books = [book for book in books if book.average_rating_value >= filter_model.min_rate_input and book.average_rating_value <= filter_model.max_rate_input]
    
    # Sort by rating
    sort_by = True if filter_model.sort_by == "good_rating" else False
    if sort_by:
        books.sort(key=lambda x: x.average_rating_value, reverse=True)

    # if current_user!= None and current_user.is_authenticated:
    #     wishlists = _wishlist_service.get_all(db, current_user.id)
    #     if wishlists:
    #         wishlists = [wishlist.book_id for wishlist in wishlists]
    #     return render_template('client/book.html',
    #                         categories = categories,
    #                         books = books,
    #                         wishlists = wishlists,
    #                         user = current_user)
    # else:
    #     return render_template('client/book.html',
    #                         categories = categories,
    #                         books = books,
    #                         user = None)
    for book in books:
        _, data = __get_star_rating_statistic(db, book.id)
        book.rating_statistic = data
        book.thumbnail_url = book.images[0].url if book.images[0] is not None else None
    
    return books
    
@router.get("/{id_or_slug}", status_code=status.HTTP_200_OK)
async def get_book_by_id(id_or_slug,
                         db: Session = Depends(get_db_context),
                         user: User = Depends(token_interceptor)) -> BookDetailViewModel:
    """ Get a book detail

    Args:
        id_or_slug (_type_): Id or slug of the book
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(token_interceptor).

    Returns:
        BookDetailViewModel: Book detail view model
    """
    book = book_service.get_by_id(db, id_or_slug)
    if not book:
        raise http_exception(404, "The book could not be found")
    
    # Book average rating
    average_rating = rating_service.get_average_rating_value_by_book(db, book.id)
    if average_rating:
        book.average_rating_value = average_rating[0].average_rating_value
        book.total_ratings = average_rating[0].total_ratings
    else:
        book.average_rating_value = None
        book.total_ratings = None

    # Book wishlist
    if not user:
        book.in_wishlist = False
    else:
        book_wishlist = wishlist_service.get_by_user_and_book(db, user.id, book.id)
        if book_wishlist:
            book.in_wishlist = True
        else:
            book.in_wishlist = False
    
    # Rating statistic
    _, data = __get_star_rating_statistic(db, book.id)
    book.rating_statistic = data
    # Book comments
    book.book_comments = rating_service.get_book_comments(db, book.id)
    
    # Book in the same category
    books_in_cat = book_service.get_books_by_cat(db, book.category_id, constants.NUMBER_OF_BOOK_IN_THE_SAME_CAT_BOOK_DETAIL_PAGE, book.id)
    __build_book_ratings(db, books_in_cat)
    book.books_in_cat = books_in_cat
    # Book related
    related_books = book_service.get_related_books(db, book.id)
    __build_book_ratings(db, related_books)
    book.related_books = related_books
            
    # Book wishlist        
    if user:
        wishlists = wishlist_service.get_all(db, user.id)
        if wishlists:
            wishlists = [wishlist.book_id for wishlist in wishlists]
    return book

@router.get('/categories/{id_or_slug}', status_code=status.HTTP_200_OK, response_model=None)
async def get_category_by_id(id_or_slug,
                              db: Session = Depends(get_db_context),
                              user: User = Depends(token_interceptor))-> CategoryDetailViewModel:
    """ Get a category detail

    Args:
        id_or_slug (_type_): Id or slug of the category
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from the JWT token. Defaults to Depends(token_interceptor).

    Raises:
        http_exception: 404 Not found

    Returns:
        CategoryDetailViewModel: Categoy detail view model
    """
    category = book_service.get_category_by_id(db, id_or_slug)
    if not category:
        raise http_exception(404, "Category could not be found")
       
    books = book_service.get_books_by_cat(db, category.id)
    __build_book_ratings(db, books)
    
    if user:
        wishlists = wishlist_service.get_all(db, user.id)
        if wishlists:
            wishlists = [wishlist.book_id for wishlist in wishlists]
            return CategoryDetailViewModel(category=category, books=books, wishlists=wishlists)
        
    return CategoryDetailViewModel(category=category, books=books)
    
@router.post("/add-wishlist/{book_id}", status_code=status.HTTP_200_OK)
async def add_book_wishlist( book_id: UUID,
                        db: Session = Depends(get_db_context),
                        user: User = Depends(token_interceptor)):
    """ Add a book to my wishlist

    Args:
        book_id (UUID): Book Id to add to wishlist
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from JWT token. Defaults to Depends(token_interceptor).

    Raises:
        http_exception: 400 Bad Request
        http_exception: 401 Not Authorized

    Returns:
        Boolean: True if success else False
    """
    if user:
        result = wishlist_service.create(db, user.id, book_id)
        if not result:
            raise http_exception(400, "Bad request")
        return result
    else:
        raise http_exception(401, "You are not authorized")
    

@router.delete('/remove-wishlist/{book_id}', status_code=status.HTTP_200_OK)
async def remove_book_from_wishlist(book_id: UUID,
                        db: Session = Depends(get_db_context),
                        user: User = Depends(token_interceptor)):
    """ Remove a book from the wishlist

    Args:
        book_id (UUID): Book Id to remove
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(token_interceptor).

    Raises:
        http_exception: 400 Bad Request
        http_exception: 401 Not Authorized

    Returns:
        Boolean: True if success else False
    """
    if user:
        result = wishlist_service.delete_by_user_and_book(db, user.id, book_id)
        if not result:
            raise http_exception(400, "Bad request")
        return result
    else:
        raise http_exception(401, "You are not authorized")

@router.post('/add-review', status_code = status.HTTP_200_OK)
async def add_rating_review(model: BookReviewCreateModel,
                        db: Session = Depends(get_db_context),
                        user: User = Depends(token_interceptor)):
    """ Add a new review/comment

    Args:
        model (BookReviewCreateModel): Review comment create model
        db (Session, optional): Db context. Defaults to Depends(get_db_context).
        user (User, optional): User from token. Defaults to Depends(token_interceptor).

    Raises:
         http_exception: 400 Bad Request
        http_exception: 401 Not Authorized

    Returns:
        Boolean: True if success else False
    """
    if user:
        result = rating_service.create_or_update(db, user.id, model.book_id, model.rating_value, model.review_comment)
        if not result:
            raise http_exception(400, "Bad request")
        return result
    else:
        raise http_exception(401, "You are not authorized")


@router.get('/star_rating_statistic/{book_id}', status_code=status.HTTP_200_OK)
async def get_star_rating_statistic(book_id: UUID,
                                    db: Session = Depends(get_db_context)) -> dict[str, float]:
    """ Get star rating for a book

    Args:
        book_id (_type_): Book id
        db (Session, optional): Db context. Defaults to Depends(get_db_context).

    Returns:
        dict[str, float]: A dictionary
    """
    _, data = __get_star_rating_statistic(db, book_id)
    return data




def __get_star_rating_statistic(db: Session, book_id):
    """
    Private method to get the star rating statistic for a book
    """
    success, results = rating_service.get_average_rating_statistic_by_book(db, book_id)
    average_rating = rating_service.get_average_rating_value_by_book(db, book_id)
    data = {
        'total_rating_1': 0,
        'total_rating_2': 0,
        'total_rating_3': 0,
        'total_rating_4': 0,
        'total_rating_5': 0,
        'total_ratings': 0,
        'average_rating': average_rating[0].average_rating_value if average_rating else 0
    }
    if results:
        for result in results:
            data['total_ratings']+= result.total_ratings
            if result.rating_value == 1.0:
                data['total_rating_1'] = result.total_ratings
            elif result.rating_value == 2.0:
                data['total_rating_2'] = result.total_ratings
            elif result.rating_value == 3.0:
                data['total_rating_3'] = result.total_ratings
            elif result.rating_value == 4.0:
                data['total_rating_4'] = result.total_ratings
            elif result.rating_value == 5.0:
                data['total_rating_5'] = result.total_ratings
    return success, data

def __build_book_ratings(db: Session, books: list[BookDetailViewModel]):
    book_ids = [book.id for book in books]
    book_average_ratings = rating_service.get_all_average_rating(db, book_ids)
    for book in books:
        book_average_rating = [book_average_rating for book_average_rating in book_average_ratings if book_average_rating.book_id == book.id]
        if book_average_rating:
            book.average_rating_value = book_average_rating[0].average_rating_value
            book.total_ratings = book_average_rating[0].total_ratings
        else:
            book.average_rating_value = None
            book.total_ratings = None