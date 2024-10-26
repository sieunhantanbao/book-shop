import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { getMyProfile, updateMyProfile } from "../../actions/auth";
import { convertToMyUserProfile, getApiUrl, getUserDetails } from "../../utils/ultil";
import { unwrapResult } from "@reduxjs/toolkit";
import { useNavigate } from "react-router-dom";

function MyProfilePage() {
  const dispatch = useDispatch();
  const imageBaseUrl = `${getApiUrl()}/static/files_uploaded`;
  const [message, setMessage] = useState({ color: "green", text: "" });
  const [userProfile, setUserProfile] = useState({}); // Ensure userProfile is initialized as an empty object
  const navigationTo = useNavigate();
  useEffect(() => {
    // If user is not logged in -> Redirect to home (do not allow the user access this page if they do not log in yet)
    var userDetail = getUserDetails();
    if (!userDetail) {
        navigationTo('/');
    }
    
    async function fetchData() {
        var result = await dispatch(getMyProfile());
        var response = unwrapResult(result);
        setUserProfile(convertToMyUserProfile(response));
    }
    fetchData();
  }, [dispatch]);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setUserProfile((values) => ({ ...values, [name]: value }));
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    const resultAction = await dispatch(updateMyProfile(userProfile));
    if (updateMyProfile.rejected.match(resultAction)) {
      setMessage({ text: "There is an error while updating my profile", color: "red" });
    } else {
      setMessage({ text: "The user profile is updated successfully", color: "green" });
    }
  };

  const renderUserPhoto = (user) => {
    if (user.photo_url) {
      return (
        <img
          id="img_user_photo"
          className="rounded-circle mt-5"
          width="150px"
          height="180px"
          src={`${imageBaseUrl}/${user.photo_url}`}
          alt="User"
        />
      );
    } else {
      return (
        <img
          id="img_user_photo"
          className="rounded-circle mt-5"
          width="150px"
          height="180px"
          src="/client/img/no-image.png"
          alt="No image"
        />
      );
    }
  };

  return (
    <>
      {userProfile && (
        <form onSubmit={handleFormSubmit}>
          <div className="row" style={{ backgroundColor: "white" }}>
            <div className="col-md-3 border-right">
              <div className="d-flex flex-column align-items-center text-center p-3 py-5">
                {renderUserPhoto(userProfile)}
                <input
                  type="file"
                  name="file_photo"
                  id="file_photo"
                  className="my-custom-file-input"
                  accept=".png,.jpg"
                />
                <span className="fw-bold">
                  {userProfile.first_name} {userProfile.last_name}
                </span>
                <span className="text-black-50">{userProfile.email}</span>
                <span> </span>
              </div>
            </div>
            <div className="col-md-5 border-right">
              <div className="p-3 py-5">
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <h4 className="text-right">Profile Settings</h4>
                </div>
                <div className="row mt-2">
                  <div className="col-md-6">
                    <label className="labels" htmlFor="first_name">
                      Name
                    </label>
                    <input
                      type="text"
                      name="first_name"
                      className="form-control"
                      onChange={handleChange}
                      value={userProfile.first_name || ''}
                      placeholder="First Name"
                    />
                  </div>
                  <div className="col-md-6">
                    <label className="labels" htmlFor="last_name">
                      Surname
                    </label>
                    <input
                      type="text"
                      name="last_name"
                      className="form-control"
                      onChange={handleChange}
                      value={userProfile.last_name || ''}
                      placeholder="Last Name"
                    />
                  </div>
                </div>
                <div className="row mt-3">
                  <div className="col-md-12">
                    <label className="labels" htmlFor="telephone">
                      Mobile Number
                    </label>
                    <input
                      type="text"
                      name="telephone"
                      className="form-control"
                      onChange={handleChange}
                      value={userProfile.telephone || ''}
                      placeholder="Telephone"
                    />
                  </div>
                  <div className="col-md-12">
                    <label className="labels" htmlFor="address">
                      Address
                    </label>
                    <textarea
                      name="address"
                      rows="5"
                      cols="45"
                      onChange={handleChange}
                      value={userProfile.address || ''}
                      placeholder="Address"
                      className="form-control"
                    ></textarea>
                  </div>
                  <div className="col-md-12">
                    <label className="labels" htmlFor="email">
                      Email Address
                    </label>
                    <input
                      type="email"
                      name="email"
                      className="form-control"
                      value={userProfile.email || ''}
                      readOnly
                      placeholder="Email Address"
                    />
                  </div>
                  <div className="col-md-12">
                    <label className="labels" htmlFor="date_of_birth">
                      Date of birth
                    </label>
                    <input
                      type="text"
                      name="date_of_birth"
                      className="form-control datetime-picker"
                      onChange={handleChange}
                      value={userProfile.date_of_birth || ''}
                      placeholder="Date of birth"
                    />
                  </div>
                </div>
                <div className="mt-2">
                  <h6 style={{ color: message.color }}>{message.text}</h6>
                </div>
                <div className="mt-5 text-center">
                  <button type="submit" className="btn btn-success">
                    Update
                  </button>
                </div>
                <div className="mt-2 text-center">
                  Need to change password? <a href="/auth/change-password">Click here</a>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="p-3 py-5">
                <div className="d-flex justify-content-between align-items-center experience">
                  <span>Edit Experience</span>
                  <span className="px-3 p-1">&nbsp;</span>
                </div>
                <br />
                <div className="col-md-12">
                  <label className="labels">Experience in</label>
                  <input
                    type="text"
                    name="experience_in"
                    onChange={handleChange}
                    value={userProfile.experience_in || ''}
                    className="form-control"
                    placeholder="Experience in"
                  />
                </div>
                <br />
                <div className="col-md-12">
                  <label className="labels">Additional Details</label>
                  <textarea
                    name="addition_detail"
                    rows="5"
                    cols="45"
                    onChange={handleChange}
                    value={userProfile.addition_detail || ''}
                    placeholder="Additional Details"
                    className="form-control"
                  ></textarea>
                </div>
              </div>
            </div>
          </div>
        </form>
      )}
    </>
  );
}

export default MyProfilePage;
