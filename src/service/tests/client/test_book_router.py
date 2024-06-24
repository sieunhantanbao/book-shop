from http.client import HTTPException
import uuid
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from datetime import datetime
from app.main import app
from app.schemas.user import User
from app.services.auth import token_interceptor
from app.database import get_db_context
from app.models.book import BookDetailViewModel, BookRelatedViewModel
from app.models.category import CategoryForDdlViewModel, CategoryViewModel
from app.models.image import ImageViewModel
from app.services import book as book_service, rating as rating_service, wishlist as wishlist_service
from fastapi import status
from uuid import UUID
import pytest
import fakeredis
from app.models.rating import BookRatingViewModel, UserInRatingViewModel
from app.schemas.wishlist import WishList
from app.models.wishlist import WishlistViewModel



################## COMMON SETUP ###############################
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

class MockBookAverageRating:
        def __init__(self, book_id: UUID, average_rating_value: float, total_ratings: int):
            self.book_id = book_id
            self.average_rating_value = average_rating_value
            self.total_ratings = total_ratings
            
# Apply the dependency overrides
app.dependency_overrides[token_interceptor] = override_token_interceptor
app.dependency_overrides[get_db_context] = override_get_db_context

client = TestClient(app)

################## TEST METHODS ###############################
def test_get_book_wishlist_success():
    # Arrange
    def mock_get_book_wishlists(db, user_id):
        return [
            BookRelatedViewModel(
                id=UUID("11111111-1111-1111-1111-111111111111"),
                title="Test Book",
                slug="test-book",
                short_description="Test short description",
                description="Test description",
                price=10.0,
                isbn="1234567890",
                author="Test Author",
                publisher="Test Publisher",
                publish_date=datetime.now(),
                pages=100,
                dimensions="10x10",
                language="English",
                thumbnail_url="https://example.com/image.png",
                sort_order=1,
                is_featured=False,
                is_published=True,
                category_id=UUID("22222222-2222-2222-2222-222222222222"),
                average_rating_value=None,
                total_ratings=None,
                in_wishlist=True,
                images=[]
            )
        ]

    # Mocking the rating_service.get_all_average_rating function
    def mock_get_all_average_rating(db, book_ids):
        return [
            MockBookAverageRating(
                book_id=UUID("11111111-1111-1111-1111-111111111111"),
                average_rating_value=4,
                total_ratings=10
            )
        ]
    
    book_service.get_book_wishlists = MagicMock(side_effect=mock_get_book_wishlists)
    rating_service.get_all_average_rating = MagicMock(side_effect=mock_get_all_average_rating)
    # Act
    response = client.get("/api/books/wishlist")
    
    # Assert
    assert response.status_code == status.HTTP_200_OK
    books = response.json()
    assert len(books) == 1
    assert books[0]["id"] == "11111111-1111-1111-1111-111111111111"
    assert books[0]["title"] == "Test Book"
    assert books[0]["average_rating_value"] == 4
    assert books[0]["total_ratings"] == 10
    
##############################################################################################
# Mock Classes
class MockCategoryView2Model:
    def __init__(self, id, name, slug, short_description, thumbnail_url, sort_order, images=None):
        self.id = id
        self.name = name
        self.slug = slug
        self.short_description = short_description
        self.thumbnail_url = thumbnail_url
        self.sort_order = sort_order
        self.images = images or []

    def as_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "slug": self.slug,
            "short_description": self.short_description,
            "thumbnail_url": self.thumbnail_url,
            "sort_order": self.sort_order,
            "images": [image.__dict__ for image in self.images]
        }

class MockImageViewModel:
    def __init__(self, id, url):
        self.id = id
        self.url = url
        
# Mocking the book_service.get_all_categories function
def mock_get_all_categories(db, limit=None):
    if limit:
        return [
            MockCategoryView2Model(
                id=UUID("11111111-1111-1111-1111-111111111111"),
                name="Category 1",
                slug="category-1",
                short_description="Short description 1",
                thumbnail_url="https://example.com/image1.png",
                sort_order=1,
                images=[MockImageViewModel(id=UUID("33333333-3333-3333-3333-333333333333"), url="https://example.com/image1.png")]
            )
        ]
    return [
        MockCategoryView2Model(
            id=UUID("11111111-1111-1111-1111-111111111111"),
            name="Category 1",
            slug="category-1",
            short_description="Short description 1",
            thumbnail_url="https://example.com/image1.png",
            sort_order=1,
            images=[MockImageViewModel(id=UUID("33333333-3333-3333-3333-333333333333"), url="https://example.com/image1.png")]
        ),
        MockCategoryView2Model(
            id=UUID("22222222-2222-2222-2222-222222222222"),
            name="Category 2",
            slug="category-2",
            short_description="Short description 2",
            thumbnail_url="https://example.com/image2.png",
            sort_order=2,
            images=[MockImageViewModel(id=UUID("44444444-4444-4444-4444-444444444444"), url="https://example.com/image2.png")]
        )
    ]
    
book_service.get_all_categories = MagicMock(side_effect=mock_get_all_categories)

@pytest.fixture(autouse=True)
def setup_and_teardown():
    with patch('app.database.redis_client') as mock_redis_client:
        mock_redis_client.get.return_value = None
        mock_redis_client.set.return_value = None
        yield mock_redis_client

@pytest.fixture
def mock_redis_client():
    redis_client = fakeredis.FakeStrictRedis()
    with patch('app.database.redis_client1', redis_client):
        yield redis_client


# def test_get_categories_all(mock_redis_client):
#     response = client.get("/api/books/categories?get_all=true")
#     assert response.status_code == 200
#     categories = response.json()
#     assert len(categories) == 2
#     assert categories[0]["id"] == "11111111-1111-1111-1111-111111111111"
#     assert categories[0]["name"] == "Category 1"
#     assert categories[0]["thumbnail_url"] == "https://example.com/image1.png"
#     assert categories[1]["id"] == "22222222-2222-2222-2222-222222222222"
#     assert categories[1]["name"] == "Category 2"
#     assert categories[1]["thumbnail_url"] == "https://example.com/image2.png"

# def test_get_categories_short(mock_redis_client):

#     response = client.get("/api/books/categories?get_all=false")
#     assert response.status_code == 200
#     categories = response.json()
#     assert len(categories) == 1
#     assert categories[0]["id"] == "11111111-1111-1111-1111-111111111111"
#     assert categories[0]["name"] == "Category 1"
#     assert categories[0]["thumbnail_url"] == "https://example.com/image1.png"

#####################################################################################
def test_get_categories_for_ddl():
    # Arrange
    def get_all_categories_for_ddl(db):
        return [
        CategoryForDdlViewModel(id=UUID("11111111-1111-1111-1111-111111111111"), name="Category 1"),
        CategoryForDdlViewModel(id=UUID("22222222-2222-2222-2222-222222222222"), name="Category 2")
    ]
    book_service.get_all_categories_for_ddl = MagicMock(side_effect=get_all_categories_for_ddl)
    
    # Act
    response = client.get("/api/books/categories-for-ddl")
    # Assert
    assert response.status_code == 200
    categories = response.json()
    assert isinstance(categories, list)
    for category in categories:
        assert "id" in category
        assert "name" in category
################################################################################
#######Todo for /api/book/featured-books########################################
################################################################################
def test_book_list_with_filter():
    # Arrange
    # Mock book_service.get_all
    def get_all(db, filter_model):
        return[
            BookDetailViewModel(
                id=UUID('12345678-1234-5678-1234-567812345678'), 
                title="Book 1",
                slug="book-1",
                price=100.5,
                isbn="ABC123456789010",
                author="Author 1",
                pages=200,
                category_id=UUID('11111111-1111-1111-1111-111111111111'),
                average_rating_value=4.5,
                images=[
                    ImageViewModel(
                        id=UUID('11111111-1111-1111-1111-111111111111'),
                        book_id=UUID('12345678-1234-5678-1234-567812345678'),
                        url="https://samplemedia.com/book1.png"
                    )
                ]
                ),
            BookDetailViewModel(
                id=UUID('87654321-4321-8765-4321-987654321098'), 
                title="Book 2",
                slug="book-2",
                price=200.5,
                isbn="DEF123456789010",
                author="Author 2",
                pages=300,
                category_id=UUID('11111111-1111-1111-1111-111111111111'),
                average_rating_value=4.0,
                images=[
                    ImageViewModel(
                        id=UUID('22222222-2222-2222-2222-222222222222'),
                        book_id=UUID('87654321-4321-8765-4321-987654321098'),
                        url="https://samplemedia.com/book2.png"
                    )
                ]
                )
        ]
    book_service.get_all = MagicMock(side_effect=get_all)
    
    def get_all_average_rating(db, book_ids):
        return [
            MockBookAverageRating(book_id=UUID('12345678-1234-5678-1234-567812345678'), average_rating_value= 4.5, total_ratings= 100),
            MockBookAverageRating(book_id=UUID('87654321-4321-8765-4321-987654321098'), average_rating_value= 3.8, total_ratings= 50),
        ]
    rating_service.get_all_average_rating = MagicMock(side_effect=get_all_average_rating)
    
    # Mock rating_service.get_average_rating_statistic_by_book
    class MockAverageRatingStatisticByBook():
        def __init__(self, total_rating_1: int,
                     total_rating_2: int,
                     total_rating_3: int,
                     total_rating_4: int,
                     total_rating_5: int,
                     total_ratings: int,
                     average_rating: float,
                     rating_value: float):
            self.total_rating_1= total_rating_1
            self.total_rating_2= total_rating_2
            self.total_rating_3= total_rating_3
            self.total_rating_4= total_rating_4
            self.total_rating_5= total_rating_5
            self.average_rating = average_rating
            self.total_ratings = total_ratings
            self.rating_value = rating_value
            
    def get_average_rating_statistic_by_book(db, book_id):
        return True, [
            MockAverageRatingStatisticByBook(
                total_rating_1 =10,
                total_rating_2 =20,
                total_rating_3 =30,
                total_rating_4 =25,
                total_rating_5 =15,
                total_ratings=100,
                average_rating=4.5,
                rating_value=4.0
        )
        ]
    rating_service.get_average_rating_statistic_by_book = MagicMock(side_effect=get_average_rating_statistic_by_book)
    
    # Act
    response = client.get('/api/books/search?min_price_input=0&max_price_input=100&min_rate_input=3&max_rate_input=5&sort_by=good_rating')
    
    # Assert
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    assert len(books) == 2
    assert books[0]['id'] == '12345678-1234-5678-1234-567812345678'
    assert books[0]['title'] == "Book 1"
    assert books[1]['id'] == '87654321-4321-8765-4321-987654321098'
    assert books[1]['title'] == "Book 2"
##################################################################################################
# Common mock/setup for get_book_by_id
# Mock rating_service.get_average_rating_value_by_book
def get_average_rating_value_by_book(db, book_id):
    return [
        MockBookAverageRating(
            book_id=UUID("12345678-1234-5678-1234-567812345678"),
            average_rating_value=4,
            total_ratings=10
        )
    ]
rating_service.get_average_rating_value_by_book = MagicMock(side_effect=get_average_rating_value_by_book)
# Mock wishlist_service.get_by_user_and_book
def get_by_user_and_book(db, id):
    return WishList(
        book_id=UUID('12345678-1234-5678-1234-567812345678'),
        user_id=UUID('11111111-1111-1111-1111-111111111111')
    )
wishlist_service.get_by_user_and_book = MagicMock(side_effect=get_by_user_and_book)
# Mock rating_service.get_average_rating_statistic_by_book
class MockAverageRatingStatisticByBook():
    def __init__(self, total_rating_1: int,
                    total_rating_2: int,
                    total_rating_3: int,
                    total_rating_4: int,
                    total_rating_5: int,
                    total_ratings: int,
                    average_rating: float,
                    rating_value: float):
        self.total_rating_1= total_rating_1
        self.total_rating_2= total_rating_2
        self.total_rating_3= total_rating_3
        self.total_rating_4= total_rating_4
        self.total_rating_5= total_rating_5
        self.average_rating = average_rating
        self.total_ratings = total_ratings
        self.rating_value = rating_value
        
def get_average_rating_statistic_by_book(db, book_id):
    return True, [
        MockAverageRatingStatisticByBook(
            total_rating_1 =10,
            total_rating_2 =20,
            total_rating_3 =30,
            total_rating_4 =25,
            total_rating_5 =15,
            total_ratings=100,
            average_rating=4.5,
            rating_value=4.0
    )
    ]
rating_service.get_average_rating_statistic_by_book = MagicMock(side_effect=get_average_rating_statistic_by_book)
# Mock rating_service.get_book_comments
def get_book_comments(db, book_id):
    return [
        BookRatingViewModel(
            id=uuid.uuid4(),
            user_id=UUID('11111111-1111-1111-1111-111111111111'),
            book_id=UUID('12345678-1234-5678-1234-567812345678'),
            rating_value=4.0,
            comment="Good book",
            is_reviewed=True,
            created_at=datetime.now(),
            user=UserInRatingViewModel(first_name="First Name", last_name="Last Name")
        )
    ]
rating_service.get_book_comments = MagicMock(side_effect=get_book_comments)
# Mock book_service.get_books_by_cat
def get_books_by_cat(db, cat_id, size: int = 0, excluded_id: UUID = None):
    return [
        BookRelatedViewModel(
        id=UUID("12345678-1234-5678-1234-567812345678"),
        title="Test Book",
        slug="test-book",
        short_description="Test short description",
        description="Test description",
        price=10.0,
        isbn="1234567890",
        author="Test Author",
        publisher="Test Publisher",
        publish_date=datetime.now(),
        pages=100,
        dimensions="10x10",
        language="English",
        thumbnail_url="https://example.com/image.png",
        sort_order=1,
        is_featured=False,
        is_published=True,
        category_id=UUID("22222222-2222-2222-2222-222222222222"),
        average_rating_value=None,
        total_ratings=None,
        in_wishlist=True,
        images=[]
        )
    ]
book_service.get_books_by_cat = MagicMock(side_effect = get_books_by_cat)
# Mocking the rating_service.get_all_average_rating function
def mock_get_all_average_rating(db, book_ids):
    return [
        MockBookAverageRating(
            book_id=UUID("12345678-1234-5678-1234-567812345678"),
            average_rating_value=4,
            total_ratings=10
        )
    ]
rating_service.get_all_average_rating = MagicMock(side_effect=mock_get_all_average_rating)
# Mock book_service.get_related_books
def get_related_books(db, book_id):
    return [
        BookRelatedViewModel(
            id=UUID("12345678-1234-5678-1234-567812345678"),
            title="Test Book",
            slug="test-book",
            short_description="Test short description",
            description="Test description",
            price=10.0,
            isbn="1234567890",
            author="Test Author",
            publisher="Test Publisher",
            publish_date=datetime.now(),
            pages=100,
            dimensions="10x10",
            language="English",
            thumbnail_url="https://example.com/image.png",
            sort_order=1,
            is_featured=False,
            is_published=True,
            category_id=UUID("22222222-2222-2222-2222-222222222222"),
            average_rating_value=None,
            total_ratings=None,
            in_wishlist=True,
            images=[]
        )
    ]
book_service.get_related_books = MagicMock(side_effect=get_related_books)
# Mock wishlist_service.get_all
def get_all_wishlist(db, user_id):
    return [
        WishlistViewModel(
            id=UUID(),
            book_id=UUID('12345678-1234-5678-1234-567812345678'),
            user_id=UUID('11111111-1111-1111-1111-111111111111')
        )
    ]
wishlist_service.get_all = MagicMock(side_effect=get_all_wishlist)

def test_get_book_by_id_success():
    # Arrange
    # Mock book_service.get_by_id
    def get_book_by_id(db, id):
        return BookDetailViewModel(
            id=UUID('12345678-1234-5678-1234-567812345678'), 
            title="Book 1",
            slug="book-1",
            price=100.5,
            isbn="ABC123456789010",
            author="Author 1",
            pages=200,
            category_id=UUID('11111111-1111-1111-1111-111111111111'),
            average_rating_value=4.5,
            images=[
                ImageViewModel(
                    id=UUID('11111111-1111-1111-1111-111111111111'),
                    book_id=UUID('12345678-1234-5678-1234-567812345678'),
                    url="https://samplemedia.com/book1.png"
                )
            ]
        )
    book_service.get_by_id = MagicMock(side_effect=get_book_by_id)
    # Act
    response = client.get('/api/books/12345678-1234-5678-1234-567812345678')
    # Assert
    assert response.status_code == 200
    book = response.json()
    assert isinstance(book, object)
    assert book["id"]=="12345678-1234-5678-1234-567812345678"
    assert book["title"]=="Book 1"


def test_get_book_by_id_not_found():
    # Arrange
    book_service.get_by_id = MagicMock(return_value=None)
    # Act
    response = client.get('/api/books/99999999-9999-9999-9999-999999999999')
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "The book could not be found"
    
###########################################################################################
# Common Mock/setup for get_category_by_id
def test_get_category_by_id_success():
    # Arrange
    def get_category_by_id(db, cat_id):
        return CategoryViewModel(
            id=UUID("22222222-2222-2222-2222-222222222222"),
            name="Category 1",
            slug="category-1",
            short_description="Short description",
            sort_order=1,
            thumbnail_url="",
            images = [
                ImageViewModel(
                    id=UUID('11111111-1111-1111-1111-111111111111'),
                    cat_id=UUID('22222222-2222-2222-2222-222222222222'),
                    url="https://samplemedia.com/category1.png"
                )
            ]
        )
    book_service.get_category_by_id = MagicMock(side_effect = get_category_by_id)
    def get_all_average_rating(db, book_ids):
        return [
            MockBookAverageRating(book_id=UUID('12345678-1234-5678-1234-567812345678'), average_rating_value= 4.5, total_ratings= 100),
            MockBookAverageRating(book_id=UUID('87654321-4321-8765-4321-987654321098'), average_rating_value= 3.8, total_ratings= 50),
        ]
    rating_service.get_all_average_rating = MagicMock(side_effect=get_all_average_rating)
    
    # Act
    response = client.get("/api/books/categories/22222222-2222-2222-2222-222222222222")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["category"]["id"] == "22222222-2222-2222-2222-222222222222" 
    assert data["category"]["name"] == "Category 1" 
    assert data["books"][0]["id"] == "12345678-1234-5678-1234-567812345678" 
    assert data["books"][0]["title"] == "Test Book" 
    

def test_get_category_by_id_not_found():
    # Arrange
    book_service.get_category_by_id = MagicMock(return_value=None)
    # Act
    response = client.get("/api/books/categories/99999999-9999-9999-9999-999999999999")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Category could not be found"