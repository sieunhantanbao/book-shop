import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchCategories } from '../../actions/categories';

// Separate component for CategoryItem
const CategoryItem = ({ category, imageBaseUrl }) => (
    <div className="col-md-2">
        <div className="row bg-white border rounded mb-3 card" style={{ height: '23rem', marginRight: '5px' }}>
            <img src={`${imageBaseUrl}/${category.thumbnail_url}`} className="card-img-top img img-responsive" style={{ height: '180px' }} alt={category.name} />
            <div className="card-body">
                <h5 className="card-title">{category.name}</h5>
                <p className="card-text">{category.short_description}</p>
                <a href={`/book/categories/${category.slug}`} className="btn btn-primary">Details</a>
            </div>
        </div>
    </div>
);

// Footer component for conditional rendering
const Footer = () => (
    <div className="card-footer">
        <div className="row">
            <div className="col-md-12">
                <a href="/book/categories/all" className="btn btn-info float-end"><small>View all</small></a>
            </div>
        </div>
    </div>
);

function CategoryList() {
    const imageBaseUrl = `${import.meta.env.VITE_API_URL}/static/files_uploaded`;
    const dispatch = useDispatch();
    const { items, loading, error } = useSelector(state => state.categories);
    const getAllCategories = false;

    useEffect(() => {
        dispatch(fetchCategories(getAllCategories));
    }, [dispatch]);

    if (loading) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div className="card">
            <div className="card-header text-black fw-bold">
                <i className="fas fa-list-alt"></i> BOOK CATEGORIES
            </div>
            <div className="card-body">
                <div className="row category-items">
                    {items.map(category => (
                        <CategoryItem key={category.id} category={category} imageBaseUrl={imageBaseUrl} />
                    ))}
                </div>
            </div>
            {!getAllCategories && <Footer />}
        </div>
    );
}

export default CategoryList;
