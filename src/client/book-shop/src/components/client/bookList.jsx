import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchSearchBooks } from '../../actions/books';
import BookItem from './sub-components/BookItem';
import BookFilter from './sub-components/BookFilter';
import './bookList.css';
function BookList({title}) {

    const [inputs, setInputs] = useState({min_rate_input:"1", max_rate_input: "5", min_price_input: "0", max_price_input: "100"});
    
    const dispatch = useDispatch();
    const { books, loadingSerachBook, errorSearchBook } = useSelector(state => state.books);

    const imageBaseUrl = `${import.meta.env.VITE_API_URL}/static/files_uploaded`;

    useEffect(() => {

        dispatch(fetchSearchBooks(inputs));

    }, [dispatch]);

    if (loadingSerachBook) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    if (errorSearchBook) return <div>Error: {errorSearchBook}</div>;

    const onFormSubmit = (event) => {
        event.preventDefault();
        dispatch(fetchSearchBooks(inputs));
    };

    return(
        <>
            <div className="card">
                <div className="card-header text-black fw-bold">
                    <i className="fas fa-book"></i> {title}
                </div>
                <div className="card-body">
                    <div className="row">
                        <div className="col-md-12 ps-0">
                            <br/>
                            <BookFilter inputs={inputs} setInputs={setInputs} handleFormSubmit={onFormSubmit} />
                        </div>
                    </div>
                    <div className="row">
                        { books.map(book => (
                            <>
                                <BookItem key={book.id} book={book} imageBaseUrl={imageBaseUrl} />
                            </>
                        ))}
                    </div>
                </div> 
            </div>
        </>
    )
}
export default BookList;