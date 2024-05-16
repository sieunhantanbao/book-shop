import React, { useState } from 'react';
import { format } from 'date-fns';
import BookRating from './BookRating';
import { useDispatch } from 'react-redux';
import { addBookToWishlist, removeBookFromWishlist } from '../../../actions/books';

function BookItem({ book, imageBaseUrl, onWishlistPage=false }) {
    const dispatch = useDispatch();
    const [isDisabled, setIsDisabled] = useState(book.in_wishlist);
    const [isRemoved, setIsRemoved] = useState(false);
    
    const handleAddWishList = (event) =>{
        event.preventDefault();
        const book_id = event.target.getAttribute("data-id");
        if (book_id){
            dispatch(addBookToWishlist(book_id));
            setIsDisabled(true);
        }
    }
    const handleRemoveWishlist = (event) => {
        event.preventDefault();
        const book_id = event.target.getAttribute("data-id");
        if (book_id){
            dispatch(removeBookFromWishlist(book_id));
            setIsRemoved(true);
        }
    }

    return (
        <>
            {isRemoved && 
                <></>
            }
            {!isRemoved && 
                <div className="col-md-6">
                    <div className="row p-2 bg-white border rounded mt-2 position-relative" style={{marginRight: '1px', height:'200px'}}>
                        { book.is_featured && 
                            <div className="ribbon-wrapper ribbon-lg">
                                <div className="ribbon text-white" style={{backgroundColor:'red'}}>
                                Featured
                                </div>
                            </div>
                        }
                        <div className="col-md-3 mt-1">
                        <a href={`/book/detail/${book.slug}`}>
                            <img className="img-fluid img-responsive rounded product-image" style={{height: '150px', width: '150px'}} src={`${imageBaseUrl}/${book.images[0].url}`} alt={book.title} />
                        </a>
                        </div>
                        <div className="col-md-6 mt-1">
                            <h5 className="text-truncate"><a href={`/book/detail/${book.slug}`} className="text-decoration-none text-dark">{book.title}</a></h5>
                            <div className="d-flex flex-row">
                                <div className="ratings mr-2">
                                    <BookRating subjectId={book.id} totalRatings={book.total_ratings} averageRatingValue={book.average_rating_value} />
                                </div>
                            </div>
                            <div className="mt-1 mb-1">
                                <i className="fas fa-user text-success"></i> <span> {book.author}</span>
                                <i className="fas fa-book text-success"></i> <span> {book.isbn}</span>
                                <i className="fas fa-newspaper text-success"></i> <span> {book.publisher}<br/></span>
                            </div>
                            <div className="mt-1 mb-1">
                                <span>{book.dimession}</span>
                                <i className="fas fa-language text-success"></i> <span> {book.language}</span>
                                <i className="fas fa-calendar text-success"></i> <span> {format(book.publish_date, "dd-MM-yyyy")}<br/></span>
                            </div>
                            <p className="text-justify text-truncate para mb-0">{book.short_description}<br/><br/></p>
                        </div>
                        <div className="align-items-center align-content-center col-md-3 border-left mt-1">
                            <div className="d-flex flex-row align-items-center">
                                <h4 className="mr-1 text-danger">${book.price}</h4>
                            </div>
                            <h6 className="text-success">Free shipping</h6>
                            <div className="d-flex flex-column mt-4">
                            <br/>
                            <a className="btn btn-primary btn-sm" href={`/book/detail/${book.slug}`}>Details</a>
                            { !onWishlistPage &&
                                <button className={`btn btn-sm mt-2 ${isDisabled ? 'btn-danger disabled' : 'btn-outline-success'}`} onClick={handleAddWishList} data-id={book.id} type="button"><i className="far fa-heart"></i></button>
                            }
                            { onWishlistPage &&
                                <button className="btn btn-sm mt-2 btn-outline-danger" onClick={handleRemoveWishlist} data-id={book.id} type="button"><i className="fa-solid fa-trash"></i></button>
                            }
                            </div>
                        </div>
                    </div>
                </div>  
            }
        </>
    );
}

export default BookItem;