import React from "react";
import { format } from 'date-fns';
import BookRating from "./sub-components/BookRating";
import SafeHtlm from "../common/SafeHtlm";
function BookDetailInfo({book}) {
    const imageBaseUrl = `${import.meta.env.VITE_API_URL}/static/files_uploaded`;

    return (
        <>
            <div className="col-md-3" style={{boxShadow: "0 -1px 6px 1px rgba(0,0,0,0.1)", marginLeft: "7px"}}>
                    <img style={{minHeight: "500px", width: "310px"}} src={`${imageBaseUrl}/${book.images[0].url}`} alt={book.title} />
                    <div className="row">
                        {book.images.map((image, index) => {
                            if (index > 0 && image.url) {
                                return (
                                    <div key={index} className="col-md-4 image-container">
                                        <img
                                            style={{ height: '80px', width: '90px' }}
                                            className="img img-fluid mt-2 border border-4 rounded-circle"
                                            src={`${imageBaseUrl}/${image.url}`}
                                            alt={book.title}
                                        />
                                        <img
                                            style={{ height: '0px', width: '0px' }}
                                            className="zoom-img float-end"
                                            src={`${imageBaseUrl}/${image.url}`}
                                            alt={book.title}
                                        />
                                    </div>
                                );
                            }
                            return null;
                        })}
                    </div>
                </div>
                <div className="col-md-6" style={{boxShadow: "0 -1px 6px 1px rgba(0,0,0,0.1)", marginLeft: "12px"}}>
                    <figure>
                    <blockquote className="blockquote mt-4">
                        <h3>{book.title}</h3>
                    </blockquote>
                    <figcaption className="blockquote-footer">
                        by <cite title="Author">{book.author}</cite>. Published on {format(book.publish_date, "dd-MM-yyyy")}
                    </figcaption>
                    </figure>
                    <div className="row">
                    <div className="col-md-5">
                        <BookRating subjectId={book.id} totalRatings={book.total_ratings} averageRatingValue={book.average_rating_value} />
                    </div>
                    </div>
                    <hr/>
                        <SafeHtlm rawHtlm={book.description} />
                    <hr/>
                    <div className="row">
                        <div className="col-md-2">
                        <small className="d-flex justify-content-center">Print length</small>
                        <br/>
                        <i className="fas fa-pager d-flex justify-content-center"></i>
                        <br/>
                        <small className="fw-bold d-flex justify-content-center">{book.pages} pages</small>
                        </div>
                        <div className="col-md-2">
                        <small className="d-flex justify-content-center">Language</small>
                        <br/>
                        <i className="fas fa-globe d-flex justify-content-center"></i>
                        <br/>
                        <small className="fw-bold d-flex justify-content-center">{book.language}</small>
                        </div>
                        <div className="col-md-2">
                        <small className="d-flex justify-content-center">Publisher</small>
                        <br/>
                        <i className="fas fa-book d-flex justify-content-center"></i>
                        <br/>
                        <small className="fw-bold d-flex justify-content-center">{book.publisher}</small>
                        </div>
                        <div className="col-md-2">
                        <small className="d-flex justify-content-center">Publication on</small>
                        <br/>
                        <i className="far fa-calendar-alt d-flex justify-content-center"></i>
                        <br/>
                        <small className="fw-bold d-flex justify-content-center">{format(book.publish_date, "dd-MM-yyyy")}</small>
                        </div>
                        <div className="col-md-2">
                        <small className="d-flex justify-content-center">Dimensions</small>
                        <br/>
                        <i className="fas fa-ruler-combined d-flex justify-content-center"></i>
                        <br/>
                        <small className="fw-bold d-flex justify-content-center">{book.dimensions}</small>
                        </div>
                        <div className="col-md-2">
                        <small className="d-flex justify-content-center">ISBN</small>
                        <br/>
                        <i className="fas fa-barcode d-flex justify-content-center"></i>
                        <br/>
                        <small className="fw-bold d-flex justify-content-center">{book.isbn}</small>
                        </div>
                    </div>
                    <br/>
                </div>
                <div className="col-md-2" style={{width:"19.33333%", boxShadow: "0 -1px 6px 1px rgba(0,0,0,0.1)", marginLeft: "12px"}}>
                        <p className="h2 text-danger fw-bold d-flex justify-content-center pt-5 pb-5">${book.price}</p>
                        <hr/>
                        <p className="ps-2">In stock: <span className="fw-bold">100</span></p>
                        <button className="btn btn-primary ms-2 w-90 mb-2">Add to Cart</button>
                        <br/>
                        <button className="btn ms-2 w-90 mb-2 btn-success"> Buy Now</button>
                        <br/>
                        <a tabIndex="0" className="ms-2 pb-3 popover-return-policy" role="button" data-bs-placement="left"  data-bs-toggle="popover" data-bs-trigger="focus" title="Return policy" data-bs-content="Return policy content"><small>Return policy</small></a>
                        <br/>
                        <a tabIndex="0" className="ms-2 pb-3 popover-payment-method" role="button" data-bs-placement="left" data-bs-toggle="popover" data-bs-trigger="focus" title="Payment methods" data-bs-content="Payment methods content"><small>Payment methods</small></a>
                        <hr/>
                        {/* {% if not book.in_wishlist %}
                        <button className="btn ms-2 w-90 mb-2 btn-warning add-to-wishlist" data-id="{{book.id}}" type="button"><i className="far fa-heart fa-2xl"></i></button>
                        {% else %}
                        <button className="btn ms-2 w-90 mb-2 btn-danger add-to-wishlist disabled" data-id="{{book.id}}" type="button"><i className="far fa-heart fa-2xl"></i></button>
                        {% endif %} */}
                </div>
        </>
    )
}
export default BookDetailInfo;