import React from 'react';
import FeaturedBookCarousel from '../../components/client/featuredBookCarousel';
import CategoryList from '../../components/client/categoryList';
import BookList from '../../components/client/bookList';
function HomePage() {
  return (
    <>
        <div className="mt-0 mb-5">
            <div className="d-flex justify-content-center row">
            <div className="col-md-12">
                <FeaturedBookCarousel></FeaturedBookCarousel>
            </div>
            <div className="col-md-12">
                <br/>
            </div>
            <div className="col-md-12">
                <CategoryList></CategoryList>
            </div>
            <div className="col-md-12">
                <br/>
            </div>
            <div className="col-md-12">
                <BookList title="BOOKS"></BookList>
                {/* {{ book.book_list(books, star_rating, wishlists, 'BOOKS', False, request.args, categories) }} */}
            </div>
            </div>
        </div>
    </>
  );
}

export default HomePage;
