
import React from 'react';
import './BookCategoryPage.css';
import CategoryList from '../../components/client/categoryList';

function BookCategoryPage() {
    return (
        <div className="mt-0 mb-5">
            <div className="d-flex justify-content-center row">
                <div className="col-md-12">
                    <CategoryList load_all={true} />
                </div>
                <div className="col-md-12">
                    <br/>
                </div>
            </div>
        </div>
  );
}

export default BookCategoryPage;
