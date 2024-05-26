import axios from 'axios';
import { JWT_REFRESH_TOKEN, JWT_TOKEN } from '../constants/constants';
import { refreshToken } from '../actions/auth';
import { unwrapResult } from '@reduxjs/toolkit';
import store from '../store';

const HttpRequestInstance = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

HttpRequestInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(JWT_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

HttpRequestInstance.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      try {
        var refresh_token = localStorage.getItem(JWT_REFRESH_TOKEN);
        if (!refresh_token){
          return Promise.reject("Don't have refresh token. Please login again");
        }
        var result = await store.dispatch(refreshToken(refresh_token));
        var response = unwrapResult(result);
        originalRequest.headers.Authorization = `Bearer ${response.data.access_token}`;
        // window.location.reload();
        return HttpRequestInstance(originalRequest);
      } catch (err) {
        return Promise.reject(err);
      }
    }
    return Promise.reject(error);
  }
);

export default HttpRequestInstance;