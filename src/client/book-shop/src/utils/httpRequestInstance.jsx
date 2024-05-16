import axios from 'axios';
import { JWT_TOKEN } from '../constants/constants';

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

export default HttpRequestInstance;