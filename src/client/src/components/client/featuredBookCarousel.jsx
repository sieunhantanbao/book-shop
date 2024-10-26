import React, { useEffect } from 'react';
import { Helmet } from 'react-helmet';
import { useDispatch, useSelector } from 'react-redux';
import { fetchFeaturedBooks } from '../../actions/books';
import { getApiUrl } from '../../utils/ultil';

const CarouselIndicators = ({ items }) => (
    <div className="carousel-indicators">
        {items.map((book, index) => (
            <button
                key={book.id}
                type="button"
                data-bs-target="#carouselBookFeatured"
                data-bs-slide-to={`${index}`}
                className={index === 0 ? 'active' : ""}
                aria-current={index === 0 ? 'true' : ''}
                aria-label={`Slide ${index + 1}`}
            />
        ))}
    </div>
);

const CarouselItems = ({ items, imageBaseUrl }) => (
    <div className="carousel-inner">
        {items.map((book, index) => (
            <div className={`carousel-item ${index === 0 ? 'active' : ''}`} key={book.id}>
                <div className="carousel-caption my-carousel-caption">
                    <h3 className="carousel-title">{book.title}</h3>
                    <h5 className="carousel-description text-truncate">{book.short_description}</h5>
                    <a href={`/book/detail/${book.slug}`} className="btn btn-lg btn-outline-warning btn-primary">Explore</a>
                </div>
            </div>
        ))}
    </div>
);

function FeaturedBookCarousel() {
    const imageBaseUrl = `${getApiUrl()}/static/files_uploaded`;
    const dispatch = useDispatch();
    const { featuredBooks, loadingFeaturedBook, errorFeaturedBook } = useSelector(state => state.books);
    useEffect(() => {
        dispatch(fetchFeaturedBooks());
    }, [dispatch]);

    if (loadingFeaturedBook) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading" />;
    if (errorFeaturedBook) return <div>Error: {errorFeaturedBook}</div>;

    const styles = featuredBooks.map((book, index) => `
        .carousel-item:nth-child(${index + 1}) {
            background-image: url('${imageBaseUrl}/${book.thumbnail_url}');
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center center;
        }
    `).join('');

    return (
        <> 
            <Helmet>
                <style>{styles}</style>
            </Helmet>
            <div id="carouselBookFeatured" className="carousel slide my-carousel">
                <CarouselIndicators items={featuredBooks} />
                <CarouselItems items={featuredBooks} imageBaseUrl={imageBaseUrl} />
                <button className="carousel-control-prev" type="button" data-bs-target="#carouselBookFeatured" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next" type="button" data-bs-target="#carouselBookFeatured" data-bs-slide="next">
                    <span className="carousel-control-next-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>
        </>
    );
}

export default FeaturedBookCarousel;
