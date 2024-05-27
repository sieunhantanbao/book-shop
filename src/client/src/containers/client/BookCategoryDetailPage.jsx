import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchCategoryDetail } from "../../actions/categories";
import { useParams } from 'react-router-dom';
import BookRelated from '../../components/client/bookRelated';
import './BookCategoryDetailPage.css';

function BookCategoryDetailPage() {
    const { cat_id } = useParams();
    
    const dispatch = useDispatch();
    const { category, loadingCategory, errorCategory } = useSelector(state => state.categories);
    useEffect(() => {
        dispatch(fetchCategoryDetail(cat_id));
    }, [dispatch]);

    const imageBaseUrl = `${import.meta.env.VITE_API_URL}/app/static/files_uploaded`;
    if (loadingCategory) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    if (errorCategory) return <div>Error: {errorCategory}</div>;
    if (category === null) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    return (
        <div className="mt-0 mb-5">
            <div className="d-flex justify-content-center row">
                <div className="col-md-12">
                    <img src={`${imageBaseUrl}/${category.category.images[0].url}`} className="img-fluid img-responsive category-banner" />
                </div>
                <div className="col-md-12">
                    <br/>
                </div>
                <div className="col-md-12">
                    <BookRelated books={category.books} title="BOOKS IN THIS CATEGORY"></BookRelated>
                </div>
            </div>
        </div>
    )
}
export default BookCategoryDetailPage;