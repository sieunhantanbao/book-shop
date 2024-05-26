import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { fetchBookWishlist } from "../../actions/books";
import BookRelated from "../../components/client/bookRelated";
import { useNavigate } from "react-router-dom";

function BookWishlistPage(){
    
    const dispatch = useDispatch();
    const { booksWishlist, loadingbooksWishlist, errorbooksWishlist } = useSelector(state => state.books);
    const navigationTo = useNavigate();
    useEffect(() =>{
        dispatch(fetchBookWishlist());
    },[dispatch]);

    if (loadingbooksWishlist) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    if (errorbooksWishlist) {
        navigationTo('/');
    }
    
    return (
        <div className="mt-0 mb-2 pt-2 pb-5 bg-white">
            <div className="row">
                <div className="col-md-12">
                    <BookRelated key="books_wishlist" title="BOOKS IN YOUR WISHLIST" books={booksWishlist} onWishlistPage={true} />
                </div>
            </div>
        </div>
    );
}
export default BookWishlistPage;