import { createAsyncThunk } from '@reduxjs/toolkit';
const apiUrl = import.meta.env.VITE_API_URL;
export const fetchCategories = createAsyncThunk(
    'categories/fetchCategories',
    async (getAll, { rejectWithValue }) => {
        try {
            const response = await fetch(`${apiUrl}/api/books/categories?get_all=${getAll}`);
            if (!response.ok) {
                throw new Error('Failed to fetch categories');
            }
            const data = await response.json();
            return data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const fetchCategories4ddl = createAsyncThunk(
    'categories/fetchCategories4ddl',
    async (args, {rejectWithValue}) => {
        try {
            const response = await fetch(`${apiUrl}/api/books/categories-for-ddl`);
            if (!response.ok){
                throw new Error('Failed to fetch categories for dropdownlist');
            }
            return await response.json();
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );