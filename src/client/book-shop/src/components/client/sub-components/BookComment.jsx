import React from "react";
import CommentRating from "./CommentRating";
import { format } from 'date-fns';

function BookComment({comments}) {
    let total_comments = comments? comments.length : 0;
    return (
        <>
            <h3>Comments (<span className="text-danger fw-bold">{total_comments}</span>)</h3> 
            { comments.map(item => (
                <div className="media" key={item.id}>
                    <div className="media-body">
                        <CommentRating ratingValue={item.rating_value} />
                        <p>{item.comment}</p>
                        <small className="text-muted float-start"><i className="fas fa-user" aria-hidden="true"></i> {item.user.first_name +' '+ item.user.last_name }</small>
                        <small className="text-muted float-end"><i className="fas fa-clock"></i>{format(item.created_at, 'MMMM dd, yyyy HH:mm:ss')}</small>
                    </div>
                </div>
            ))}
        </>
    );
}
export default BookComment;