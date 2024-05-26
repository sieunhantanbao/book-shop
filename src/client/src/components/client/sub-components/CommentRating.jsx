import React from 'react';

const CommentRating = ({ ratingValue = 0 }) => {
    const starMeanings = ['Bad', 'Poor', 'Average', 'Great', 'Excellent'];

    return (
        <div className="float-start rating" title="Customer rating">
            {starMeanings.map((meaning, index) => (
                <div key={index} className="star" style={{ fontSize: '15px' }}>
                    {ratingValue < index + 1 ? (
                        <span className="full" data-value={index + 1} title={meaning}></span>
                    ) : (
                        <span className="full star-colour" data-value={index + 1} title={meaning}></span>
                    )}
                    <span className="selected"></span>
                </div>
            ))}
        </div>
    );
};

export default CommentRating;
