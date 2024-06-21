from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from datetime import datetime
from app.main import app
from app.schemas.user import User
from app.services.auth import token_interceptor
from app.database import get_db_context
from app.models.book import BookRelatedViewModel
from app.services import book as book_service, rating as rating_service
from fastapi import status
from uuid import UUID
import pytest
import fakeredis

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
    
    # Mock Class for Rating
    class MockBookAverageRating:
        def __init__(self, book_id: UUID, average_rating_value: float, total_ratings: int):
            self.book_id = book_id
            self.average_rating_value = average_rating_value
            self.total_ratings = total_ratings

    # Mocking the rating_service.get_all_average_rating function
    def mock_get_all_average_rating(db, book_ids):
        return [
            MockBookAverageRating(
                book_id=UUID("11111111-1111-1111-1111-111111111111"),
                average_rating_value=4.5,
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
    assert books[0]["average_rating_value"] == 4.5
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