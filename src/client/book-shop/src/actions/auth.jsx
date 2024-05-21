import { createAsyncThunk } from '@reduxjs/toolkit';
import HttpRequestInstance from '../utils/httpRequestInstance';

export const registerUser = createAsyncThunk(
  'auths/registerUser',
  async (agrs, { rejectWithValue }) => {
    try {
      const response = await HttpRequestInstance.post(`/api/users`,
        {
          email: agrs.email,
          first_name: agrs.first_name,
          last_name: agrs.last_name,
          is_active: agrs.is_active,
          is_admin: agrs.is_admin,
          password: agrs.password,
          confirm_password: agrs.confirm_password
        });
      if (!response.data) {
        throw new Error('Error while creating a new user');
      }
      return response.data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const login = createAsyncThunk(
  'auths/login',
  async (formData, { rejectWithValue }) => {
    try {
      const body = new URLSearchParams(formData).toString();
      const response = await HttpRequestInstance.post(`/auth/token`, body, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
      });
      if (!response.data.access_token) {
        throw new Error('Email or password is incorrect');
      }
      return response.data.access_token;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const logout = createAsyncThunk(
  'auths/logout',
  async (agrs, { rejectWithValue }) => {
    try {
      // TODO: Logout from the server if required
      return "ok";
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const changePassword = createAsyncThunk(
  'auths/changePassword',
  async (agrs, { rejectWithValue }) => {
    var response = null;
    try {
      response = await HttpRequestInstance.post(`/api/users/change-password`,
        {
          email: agrs.email,
          old_password: agrs.current_password,
          new_password: agrs.new_password,
          confirm_new_password: agrs.confirm_new_password
        });
      return { data: response.data, status: response.status };
    } catch (error) {
      if (error.response) {
        if (error.response.data.detail.constructor.name == "Array") {
          return rejectWithValue({ message: error.response.data.detail[0].msg, status: error.response.status });
        } else {
          return rejectWithValue({ message: error.response.data.detail, status: error.response.status });
        }
        // Server responded with a status other than 200 range
        
      } else if (error.request) {
        // Request was made but no response received
        return rejectWithValue({ message: "No response received from server", status: null });
      } else {
        // Something happened in setting up the request that triggered an error
        return rejectWithValue({ message: error.message, status: null });
      }
    }
  }
);

export const getMyProfile = createAsyncThunk(
  'auths/getMyProfile',
  async (agrs, { rejectWithValue }) => {
    try {
      const response = await HttpRequestInstance.get(`/api/users/profile`);
      if (!response.data) {
        throw new Error('Error while getting my profile');
      }
      return response.data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const updateMyProfile = createAsyncThunk(
  'auths/updateMyProfile',
  async (agrs, { rejectWithValue }) => {
    try {
      const response = await HttpRequestInstance.post(`/api/users/profile`, {
        email: agrs.email,
        first_name: agrs.first_name,
        last_name: agrs.last_name,
        telephone: agrs.telephone,
        address: agrs.address,
        experience_in: agrs.experience_in,
        addition_detail: agrs.addition_detail,
        date_of_birth: agrs.date_of_birth
      });
      if (response.status == 403) {
        throw new Error("Your are not authorized to perform this action")
      }
      if (response.status == 404) {
        throw new Error("User does not exist")
      }
      if (response.status == 500) {
        throw new Error("There was an error while updating user profile")
      }
      if (!response.data) {
        throw new Error('Error while updating my profile');
      }
      return response.data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);