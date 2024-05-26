import React, { useState, useEffect } from 'react';
import './RatingDetail.css';
import BookRating from './BookRating';
import HttpRequestInstance from '../../../utils/httpRequestInstance';

const RatingDetail = ({ bookId }) => {
    const [ratingData, setRatingData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    useEffect(() => {
        if (!bookId) return;
        const fetchRatingData = async () => {
            setLoading(true);
            try {
                const response = await HttpRequestInstance.get(`/api/books/star_rating_statistic/${bookId}`);
                if(response){
                    setRatingData(response.data);
                    setLoading(false);
                }else{
                    setError("There was an error while loading star ratings");
                }
            } catch (err) {
                setError(err.message);
                setLoading(false);
            }
        };
        fetchRatingData();
    }, [bookId]);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;

    const renderRatingDetail = () => {
        if (!ratingData) return null;
        return (
            <div>
                <div className="row">
                    <div className="col-md-12">
                        <BookRating subjectId={bookId} totalRatings={ratingData.total_ratings} averageRatingValue={ratingData.average_rating} showScore={false} />
                        <p className="float-end rating-header mt-1">
                            <span className="fw-bold text-success">{ratingData.average_rating.toFixed(2)}</span> out of 5 (with <span className="fw-bold text-danger">{ratingData.total_ratings}</span> global ratings)
                        </p>
                    </div>
                </div>
                {Array.from({ length: 5 }, (_, i) => (
                    <div className="row pt-2" key={i}>
                        <div className="col-md-2">{5 - i} stars</div>
                        <div className="col-md-7">
                            <div className="progress">
                                <div
                                    className={`progress-bar bg-warning w-${Math.round((ratingData[`total_rating_${5 - i}`] / ratingData.total_ratings) * 100)}%`}
                                    role="progressbar"
                                    style={{ width: `${Math.round((ratingData[`total_rating_${5 - i}`] / ratingData.total_ratings) * 100)}%` }}
                                    aria-valuenow={Math.round((ratingData[`total_rating_${5 - i}`] / ratingData.total_ratings) * 100)}
                                    aria-valuemin="0"
                                    aria-valuemax="100"
                                >
                                    {(ratingData[`total_rating_${5 - i}`] / ratingData.total_ratings * 100).toFixed(1)}%
                                </div>
                            </div>
                        </div>
                        <div className="col-md-3">
                            (<span className="fw-bold text-success">{ratingData[`total_rating_${5 - i}`]}</span> votes)
                        </div>
                    </div>
                ))}
                <hr />
            </div>
        );
    };

    return (
        <div>
            {renderRatingDetail()}
        </div>
    );
};

export default RatingDetail;
