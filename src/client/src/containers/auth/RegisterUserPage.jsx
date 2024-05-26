import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { registerUser } from "../../actions/auth";
import { useNavigate } from 'react-router-dom';
import { getUserDetails } from "../../utils/ultil";

function RegisterUserPage() {
    const [inputs, setInputs] = useState({});
    const [errors, setErrors] = useState({});
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const error = useSelector(state => state.auths.errorRegisterUserResult);

    useEffect(() => {
        const userDetail = getUserDetails();
        if (userDetail) {
            navigate('/');
        }
    }, [navigate]);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setInputs(values => ({ ...values, [name]: value }));
    }

    const validateForm = () => {
        const newErrors = {};
        if (!inputs.email) newErrors.email = 'Please provide an email.';
        if (!inputs.password) newErrors.password = 'Please provide a password.';
        if (inputs.password !== inputs.confirm_password) newErrors.confirm_password = 'Passwords do not match.';
        return newErrors;
    };

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        const formErrors = validateForm();
        if (Object.keys(formErrors).length > 0) {
            setErrors(formErrors);
            return;
        }
        try {
            await dispatch(registerUser(inputs));
            if (!error) {
                navigate('/auth/login');
            }
        } catch {
            setErrors({ general: 'Email or password is incorrect.' });
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
                                            <h4 className="mt-1 mb-5 pb-1">Book store Online</h4>
                                        </div>
                                        <form onSubmit={handleFormSubmit}>
                                            <p>Please fill below information</p>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-4">
                                                    <label className="col-form-label" htmlFor="email">Email</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-8">
                                                    <input type="email" name="email" value={inputs.email || ''} onChange={handleChange} className="form-control" placeholder="Email Address" />
                                                    {errors.email && <div className="text-danger">{errors.email}</div>}
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-4">
                                                    <label className="col-form-label" htmlFor="first_name">First Name</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-8">
                                                    <input type="text" name="first_name" value={inputs.first_name || ''} onChange={handleChange} className="form-control" placeholder="First Name" />
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-4">
                                                    <label className="col-form-label" htmlFor="last_name">Last Name</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-8">
                                                    <input type="text" name="last_name" value={inputs.last_name || ''} onChange={handleChange} className="form-control" placeholder="Last Name" />
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-4">
                                                    <label className="col-form-label" htmlFor="password">Password</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-8">
                                                    <input type="password" name="password" value={inputs.password || ''} onChange={handleChange} className="form-control" placeholder="Password" />
                                                    {errors.password && <div className="text-danger">{errors.password}</div>}
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-4">
                                                    <label className="col-form-label" htmlFor="confirm_password">Confirm Password</label>
                                                    <span className="required-asterisk">*</span>
                                                </div>
                                                <div className="col-md-8">
                                                    <input type="password" name="confirm_password" value={inputs.confirm_password || ''} onChange={handleChange} className="form-control" placeholder="Confirm Password" />
                                                    {errors.confirm_password && <div className="text-danger">{errors.confirm_password}</div>}
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-4">
                                                    <button type="submit" className="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3">Register</button>
                                                </div>
                                            </div>
                                            <div className="form-group row mt-3">
                                                <div className="col-md-12">
                                                    Have an account? <a href="/auth/login" className="btn btn-outline-danger">Login now</a>
                                                </div>
                                            </div>
                                            {errors.general && <div className="text-danger">{errors.general}</div>}
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

export default RegisterUserPage;
