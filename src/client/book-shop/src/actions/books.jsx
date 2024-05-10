import { createAsyncThunk } from '@reduxjs/toolkit';
const apiUrl = import.meta.env.VITE_API_URL;
export const fetchFeaturedBooks = createAsyncThunk(
    'books/fetchFeaturedBooks',
    async (args, { rejectWithValue }) => {
        try {
            const response = await fetch(`${apiUrl}/api/books/featured-books`);
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

export const fetchSearchBooks = createAsyncThunk(
    'books/fetchSearchBooks',
    async (args, {rejectWithValue}) => {
        try {
            const response = await fetch(`${apiUrl}/api/books/search?min_price_input=${args.min_price_input}&max_price_input=${args.max_price_input}&min_rate_input=${args.min_rate_input}&max_rate_input=${args.max_rate_input}&sort_by=${args.sort_by!=undefined?args.sort_by:''}&keyword=${args.keyword!=undefined?args.keyword:''}&category=${args.category!=undefined?args.category:''}`);
            if (!response.ok){
                throw new Error('Failed to fetch Books');
            }
            return await response.json();
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );