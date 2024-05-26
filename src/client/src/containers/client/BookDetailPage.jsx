
import BookRelated from '../../components/client/bookRelated';
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchBookDetail } from '../../actions/books';
import { useParams } from 'react-router-dom';
import BookDetailInfo from '../../components/client/bookDetailInfo';
import RatingDetail from '../../components/client/sub-components/RatingDetail';
import BookComment from '../../components/client/sub-components/BookComment';
import BookReviewForm from '../../components/client/sub-components/BookReviewForm';

import './BookDetailPage.css';

function BookDetailPage() {

    const { book_id } = useParams();
    
    const dispatch = useDispatch();
    const { bookDetail, loadingbookDetail, errorbookDetail } = useSelector(state => state.books);
    useEffect(() => {
        dispatch(fetchBookDetail(book_id));
    }, [dispatch]);

    if (loadingbookDetail) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    if (errorbookDetail) return <div>Error: {errorbookDetail}</div>;
    if (bookDetail === null) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;

    return (
        <div className="mt-0 mb-2 pt-2 pb-5 bg-white">
            <div className="row">
                <BookDetailInfo book={bookDetail} />
            </div>
            <hr/>
            <div className="row">
                <div className="col-md-12">
                    <BookRelated key="books_related" title="BOOKS RELATED" books={bookDetail.related_books} />
                </div>
            </div>

            <div className="row">
                <div className="col-md-12">
                    <BookRelated key="books_same_cat" title="BOOKS IN SAME CATEGORY" books={bookDetail.books_in_cat} />
                </div>
            </div>
            <hr/>
            <div className="d-flex justify-content-center row">
                <div className="col-md-4">
                <div className="row">
                    <div className="col-md-12 customer-review-box">
                        <h3>Customer Reviews</h3>
                        <div className="ps-3">
                            <RatingDetail bookId={bookDetail.id} />
                        </div>
                        <BookReviewForm />
                    </div>
                </div>
                </div>
                <div className="col-md-8">
                <div className="row">
                    <div className="col-md-12 pe-4">
                        <section className="content-item" id="comments">
                        <div className="container">   
                            <div className="row">
                                <div className="col-sm-12 col-md-12">
                                    <BookComment comments={bookDetail.book_comments} />
                                </div>
                            </div>
                        </div>
                    </section>
                    </div>
                </div>
                </div>
            </div>
        </div>
  );
}

export default BookDetailPage;
