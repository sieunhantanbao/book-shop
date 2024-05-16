import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { login } from "../../actions/auth";
import { useNavigate } from 'react-router-dom';
import { getUserDetails } from "../../utils/ultil";
function LoginPage() {

    const [inputs, setInputs] = useState('');
    const dispatch = useDispatch();
    const navigationTo = useNavigate();
    const loading = useSelector(state => state.auths.loading);
    const error = useSelector(state => state.auths.error);
    const isAuthenticated = useSelector(state => state.auths.isAuthenticated);

    useEffect(() => {
        if (isAuthenticated) {
            navigationTo('/');
        }
        // If the user already logged in -> redirect to home page
        var userDetail = getUserDetails();
        if (userDetail) {
            navigationTo('/');
        }
    }, [isAuthenticated, dispatch]);


    const handleChange = (event) => {
        const name = event.target.name;
        const value = event.target.value;
        setInputs(values => ({ ...values, [name]: value }));
    }

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        if (!inputs.email || !inputs.password) {
            setInputs('Please provide both email and password.');
            return;
        }
        try {
            await dispatch(login({ username: inputs.email, password: inputs.password }));
        } catch (error) {
            setInputs('Email or password is incorrect.');
        }
    };

    return (
        <section className="h-100 gradient-form">
            <div className="container py-5 h-100">
                <div className="row d-flex justify-content-center align-items-center h-100">
                    <div className="col-xl-10">
                        <div className="card rounded-3 text-black">
                            <div className="row g-0">
                                <div className="col-lg-6">
                                    <div className="card-body p-md-5 mx-md-4">
                                        <div className="text-center">
                                            <img src="/client/img/logo.jpg" style={{ width: "185px" }} alt="logo" />
                                            <h4 className="mt-1 mb-5 pb-1">Book Shop Online</h4>
                                        </div>
                                        <form onSubmit={handleFormSubmit}>
                                            <p>Please login to your account</p>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-3">
                                                    <label className="col-form-label" htmlFor="email">Email</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-9">
                                                    <input type="email" name="email" value={inputs.email || ""} onChange={handleChange} className="form-control" placeholder="Email Address" />
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-3">
                                                    <label className="col-form-label" htmlFor="password">Password</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-9">
                                                    <input type="password" name="password" value={inputs.password || ""} onChange={handleChange} className="form-control" placeholder="Password" />
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-12">
                                                    {error && <div className="text-danger">{error}</div>}
                                                    <button type="submit" disabled={loading} className="btn btn-primary gradient-custom-2 mb-3">Login</button>
                                                    <a className="text-muted" href="#">Forgot password?</a>
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-12">
                                                    Don't have an account? <a href="/auth/register" className="btn btn-outline-danger">Register Now</a>
                                                </div>
                                            </div>
                                        </form>

                                    </div>
                                </div>
                                <div className="col-lg-6 d-flex align-items-center gradient-custom-2">
                                    <div className="text-white px-3 py-4 p-md-5 mx-md-4">
                                        <h4 className="mb-4">We are more than just a bookstore</h4>
                                        <p className="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                                            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                                            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
export default LoginPage;