import React from 'react';
import BookItem from './sub-components/BookItem';
function BookRelated({title, books, onWishlistPage=false}) {
    const imageBaseUrl = `${import.meta.env.VITE_API_URL}/static/files_uploaded`;

    if (!books) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;

    return(
        <>
            <div className="card">
                <div className="card-header text-black fw-bold">
                    <i className="fas fa-book"></i> {title}
                </div>
                <div className="card-body">
                    <div className="row">
                        { books.map(book => (
                                <BookItem key={book.id} book={book} imageBaseUrl={imageBaseUrl} onWishlistPage={onWishlistPage} />
                        ))}
                    </div>
                </div> 
            </div>
        </>
    )
}
export default BookRelated;