import { createAsyncThunk } from '@reduxjs/toolkit';
import HttpRequestInstance from '../utils/httpRequestInstance';
const apiUrl = import.meta.env.VITE_API_URL;
export const fetchCategories = createAsyncThunk(
    'categories/fetchCategories',
    async (getAll, { rejectWithValue }) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/categories?get_all=${getAll}`);
            if (!response) {
                throw new Error('Failed to fetch categories');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const fetchCategories4ddl = createAsyncThunk(
    'categories/fetchCategories4ddl',
    async (args, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/categories-for-ddl`);
            if (!response){
                throw new Error('Failed to fetch categories for dropdownlist');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );

 export const fetchCategoryDetail = createAsyncThunk(
    'categories/fetchCategoryDetail',
    async (cat_id, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/categories/${cat_id}`);
            if (!response){
                throw new Error('Failed to fetch category detail');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );