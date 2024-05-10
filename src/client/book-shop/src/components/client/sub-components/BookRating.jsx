import React from 'react';
import './BookRating.css';

function BookRating({ subjectId, totalRatings, averageRatingValue }) {
    averageRatingValue = averageRatingValue || 0;

    const stars = [];
    for (let i = 1; i <= 5; i++) {
        if (averageRatingValue >= i) {
            stars.push(<span key={`full-${i}`} className="full star-colour" data-value={i}></span>);
        } else if (averageRatingValue >= i - 0.5) {
             stars.push(<span key={`half-${i}`} className="half star-colour" data-value={i - 0.5}></span>);
        } else {
            stars.push(<span key={`empty-${i}`} className="full" data-value={i}></span>);
        }
    }

    return (
        <div className="rating" data-id={subjectId} title="Book rating">
            {stars.map(star => (
                <div className="star" key={`star-${star.props['data-value']}`}>
                    {star}
                    <span className="selected"></span>
                </div>
            ))}
            <div className="score">
                {averageRatingValue > 0 ? (
                    <>
                        <span className="score-rating">{averageRatingValue.toFixed(2)}</span>
                        <span className="score-rating-average-text">({totalRatings} ratings)</span>
                    </>
                ) : (
                    <>
                        <span className="score-rating">N/A</span>
                        <span className="score-rating-average-text">(0 rating)</span>
                    </>
                )}
            </div>
        </div>
    );
}

export default BookRating;
