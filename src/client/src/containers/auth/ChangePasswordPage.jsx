import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { changePassword } from "../../actions/auth";
import { getUserDetails } from "../../utils/ultil";
import { useNavigate } from "react-router-dom";
import { unwrapResult } from "@reduxjs/toolkit";

function ChangePasswordPage() {
    const [inputs, setInputs] = useState({ current_password: "", new_password: "", confirm_new_password: "", email: "" });
    const dispatch = useDispatch();
    const [inputError, setInputError] = useState();
    const navigationTo = useNavigate();

    useEffect(() => {
        // If user is not logged in -> Redirect to home (do not allow the user access this page if they do not log in yet)
        var userDetail = getUserDetails();
        if (!userDetail) {
            navigationTo('/');
        }
        setInputs(values => ({ ...values, email: userDetail.email }));
    }, []);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setInputs(values => ({ ...values, [name]: value }));
    }

    const handleFormSubmit = async (event) => {
        event.preventDefault();
        if (!inputs.current_password) {
            setInputError("Current password could not be empty");
            return;
        }
        if (inputs.new_password != inputs.confirm_new_password) {
            setInputError("The new password and confirm password does not match");
            return;
        }
        try {
            var result = await dispatch(changePassword(inputs));
            unwrapResult(result);
            navigationTo("/");
        } catch (error) {
            setInputError(error.message);
        }
    }

    return (
        <div className="row" style={{ backgroundColor: "white" }}>
            <div className="col-md-4">
                &nbsp;
            </div>
            <div className="col-md-4">
                <br />
                <br />
                <form onSubmit={handleFormSubmit}>
                    <div className="form-group row">
                        <div className="col-md-12">
                            <h3>Change your password</h3>
                        </div>
                    </div>
                    <div className="form-group row mt-3">
                        <div className="col-md-4">
                            <label className="col-form-label" htmlFor="current_password">Current password</label>
                            <span className="required-asterisk">*</span>
                        </div>
                        <div className="col-md-8">
                            <input type="password" name="current_password" value={inputs.current_password} onChange={handleChange} className="form-control" placeholder="Current Password" />
                        </div>
                    </div>
                    <div className="form-group row mt-3">
                        <div className="col-md-4">
                            <label className="col-form-label" htmlFor="new_password">New Password</label>
                            <span className="required-asterisk">*</span>
                        </div>
                        <div className="col-md-8">
                            <input type="password" name="new_password" value={inputs.new_password} onChange={handleChange} className="form-control" placeholder="New Password" />
                        </div>
                    </div>
                    <div className="form-group row mt-3">
                        <div className="col-md-4">
                            <label className="col-form-label" htmlFor="confirm_new_password">Confirm Password</label>
                            <span className="required-asterisk">*</span>
                        </div>
                        <div className="col-md-8">
                            <input type="password" name="confirm_new_password" value={inputs.confirm_new_password} onChange={handleChange} className="form-control" placeholder="Confirm New Password" />
                        </div>
                    </div>
                    <div className="form-group row mt-3">
                        <div className="col-md-12">
                            {inputError && <div className="text-danger">{inputError}</div>}
                        </div>
                    </div>
                    <div className="form-group row mt-3">
                        <div className="col-md-4">
                            <button type="submit" className="btn btn-primary btn-block gradient-custom-2 mb-3">Update</button>
                        </div>
                    </div>
                </form>
            </div>
            <div className="col-md-4">
                &nbsp;
            </div>
        </div>
    )
}
export default ChangePasswordPage;