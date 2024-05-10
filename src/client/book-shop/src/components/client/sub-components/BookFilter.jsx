import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchCategories4ddl } from '../../../actions/categories';
import SelectField from './SelectField';

function BookFilter({inputs, setInputs, handleFormSubmit}) {

    const dispatch = useDispatch();
    const { ddlItems, ddlLoading, error } = useSelector(state => state.categories);

    const max_price_input_start_allowed = 500;
    const max_price_input_end_allowed = 500;
    const max_rate_input_start_allowed = 5;
    const max_rate_input_end_allowed = 5;

    useEffect(() => {

        dispatch(fetchCategories4ddl());

    }, [dispatch]);

    const [checkedState, setCheckedState] = useState(
        ddlItems.reduce((acc, item) => ({
            ...acc,
            [item.id]: false
        }), {})
    );

    if (ddlLoading) return <img src="/client/img/loading_icon.gif" height="64" width="64" alt="Loading"/>;
    if (error) return <div>Error: {error}</div>;

    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({...values, [name]: value}));
    }
    
    const handleCheckboxChange = (event) => {
        const { value, checked } = event.target;
        setCheckedState(prevState => ({
            ...prevState,
            [value]: checked
        }));
        // Immediately compute the new category selection without waiting for state to update
        setInputs(prevInputs => {
            const newCheckedState = {
                ...checkedState,
                [value]: checked
            };
            const selectedCategories = Object.entries(newCheckedState)
                .filter(([key, val]) => val)
                .map(([key]) => key.replace('cat_', ''));
            return {
                ...prevInputs,
                'category': selectedCategories.join(',')
            };
        });
    };

    return(
        <>
            <form onSubmit={(event) => handleFormSubmit(event)}>
                <div className="card">
                    <div className="card-body">
                        <div className="row mb-3">
                            <div className="col-md-1">
                                <strong>Keyword</strong>
                            </div>
                            <div className="col-md-5">
                                <input type="text" 
                                    className="form-control form-control-sm"
                                    placeholder="Keyword"
                                    name="keyword"
                                    value={inputs.keyword || ""} 
                                    onChange={handleChange}/>
                            </div>
                            <div className="col-md-1">
                                <strong>Sort by</strong>
                            </div>
                            <div className="col-md-5">
                                <SelectField name="sort_by" value={inputs.sort_by || ""} onChange={handleChange} options={[
                                        { label: "---Sort by---", value: "" },
                                        { label: "Price high to low", value: "price_high_low" },
                                        { label: "Price low to high", value: "price_low_high" },
                                        { label: "Good Rating", value: "good_rating" },
                                        { label: "Featured book", value: "featured" }
                                    ]} />
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-1">
                                <br/>
                                <strong>Category</strong>
                            </div>
                            <div className="col-md-10">
                            <div className="row">
                                {ddlItems.map(category => (
                                    <div className="col-md-2 form-check form-check-inline" key={category.id}>
                                        <input className="form-check-input" 
                                            name="category" 
                                            type="checkbox" 
                                            id={`cat_${category.id}`} 
                                            value={`cat_${category.id}`}
                                            checked={checkedState[category.id]}
                                            onChange={handleCheckboxChange}
                                        />
                                        <label className="form-check-label" htmlFor={`cat_${category.id}`}>{category.name}</label>
                                    </div>
                                ))}
                            </div>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-md-12"><br/></div>
                        </div>
                        <div className="row">
                            <div className="col-md-1">
                                <br/>
                                <strong>Rice range</strong>
                            </div>
                            <div className="col-md-5">
                                <div className="custom-wrapper">
                                    <div className="price-input-container">
                                        <div className="row">
                                            <div className="price-input  col-md-2">
                                                <div className="price-field"> 
                                                <input type="number"
                                                    className="min-price-input"
                                                    value={inputs.min_price_input || "0"}
                                                    name="min_price_input"
                                                    onChange={handleChange}  /> 
                                                </div>
                                            </div>
                                            <div className="col-md-8">
                                            </div>
                                            <div className="price-input  col-md-2">
                                                <div className="price-field"> 
                                                <input type="number"
                                                    className="max-price-input"
                                                    value={inputs.max_price_input || "200"}
                                                    name="max_price_input"
                                                    onChange={handleChange} /> 
                                                </div>
                                            </div> 
                                        </div>
                                        <div className="slider-container"> 
                                            <div className="price-slider" style={{
                                                                            left: `${(inputs.min_price_input / max_price_input_start_allowed) * 100}%`, 
                                                                            right: `${100 - (inputs.max_price_input / max_price_input_end_allowed) * 100}%`
                                                                        }}> 
                                            </div> 
                                        </div> 
                                    </div> 
                                    <div className="range-price-input"> 
                                        <input type="range"
                                            className="min-price"
                                            min="1"
                                            max={max_price_input_start_allowed}
                                            value={inputs.min_price_input || "0"}
                                            step="1"
                                            name="min_price_input"
                                            onChange={handleChange}
                                                /> 
                                        <input type="range"
                                            className="max-price"
                                            min="1"
                                            max={max_price_input_end_allowed}
                                            value={inputs.max_price_input || "200"}
                                            step="1"
                                            name="max_price_input"
                                            onChange={handleChange}
                                                /> 
                                    </div> 
                                </div> 
                            </div>
                            <div className="col-md-1">
                                <br/>
                                <strong>Ratings</strong>
                            </div>
                            <div className="col-md-5">
                                <div className="custom-wrapper">
                                    <div className="rate-input-container">
                                        <div className="row">
                                            <div className="rate-input  col-md-2">
                                                <div className="rate-field"> 
                                                    <input type="number"
                                                        className="min-rate-input"
                                                        value={inputs.min_rate_input || "0"}
                                                        name="min_rate_input"
                                                        onChange={handleChange}/> 
                                                </div>
                                            </div>
                                            <div className="col-md-8">
                                            </div>
                                            <div className="rate-input  col-md-2">
                                                <div className="rate-field"> 
                                                    <input type="number"
                                                        className="max-rate-input"
                                                        value={inputs.max_rate_input || "5"}
                                                        name="max_rate_input"
                                                        onChange={handleChange}/> 
                                                </div>
                                            </div> 
                                        </div>
                                        <div className="slider-container"> 
                                            <div className="rate-slider"  style={{
                                                                            left: `${(inputs.min_rate_input / max_rate_input_start_allowed) * 100}%`, 
                                                                            right: `${100 - (inputs.max_rate_input / max_rate_input_end_allowed) * 100}%`
                                                                        }}>  
                                            </div> 
                                        </div> 
                                    </div> 
                                    <div className="range-rate-input"> 
                                        <input type="range"
                                            className="min-rate"
                                            min="0"
                                            max={max_rate_input_start_allowed}
                                            value={inputs.min_rate_input || "0"}
                                            step="1"
                                            name="min_rate_input"
                                            onChange={handleChange}
                                                /> 
                                        <input type="range"
                                            className="max-rate"
                                            min="0"
                                            max={max_rate_input_end_allowed}
                                            value={inputs.max_rate_input || "5"}
                                            step="1"
                                            name="max_rate_input"
                                            onChange={handleChange}
                                                /> 
                                    </div> 
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="card-footer">
                        <button type="submit" className="btn btn-success float-end btn-sm">Apply</button>
                    </div>
                </div>
            </form>
        </>
    )
}
export default BookFilter;