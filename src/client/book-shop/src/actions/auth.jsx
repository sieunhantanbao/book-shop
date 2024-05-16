import { createAsyncThunk } from '@reduxjs/toolkit';
import HttpRequestInstance from '../utils/httpRequestInstance';

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