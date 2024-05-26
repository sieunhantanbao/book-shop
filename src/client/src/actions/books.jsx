import { createAsyncThunk } from '@reduxjs/toolkit';
import HttpRequestInstance from '../utils/httpRequestInstance';
export const fetchFeaturedBooks = createAsyncThunk(
    'books/fetchFeaturedBooks',
    async (args, { rejectWithValue }) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/featured-books`);
            if (!response) {
                throw new Error('Failed to fetch categories');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
);

export const fetchSearchBooks = createAsyncThunk(
    'books/fetchSearchBooks',
    async (args, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/search?min_price_input=${args.min_price_input}&max_price_input=${args.max_price_input}&min_rate_input=${args.min_rate_input}&max_rate_input=${args.max_rate_input}&sort_by=${args.sort_by!=undefined?args.sort_by:''}&keyword=${args.keyword!=undefined?args.keyword:''}&category=${args.category!=undefined?args.category:''}`);
            if (!response){
                throw new Error('Failed to fetch Books');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );

export const fetchBookDetail = createAsyncThunk(
    'books/fetchBookDetail',
    async (book_id_or_slug, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/${book_id_or_slug}`);
            if (!response){
                throw new Error('Failed to fetch Book');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );

 export const fetchBookWishlist = createAsyncThunk(
    'books/fetchBookWishlist',
    async (args, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.get(`/api/books/wishlist`);
            if (!response){
                throw new Error('Failed to fetch Book');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );

 export const addBookToWishlist = createAsyncThunk(
    'books/addBookToWishlist',
    async (book_id, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.post(`/api/books/add-wishlist/${book_id}`, null);
            if (!response){
                throw new Error('Failed to add the book to wishlist');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );

export const removeBookFromWishlist = createAsyncThunk(
    'books/removeBookFromWishlist',
    async (book_id, {rejectWithValue}) => {
        try {
            const response = await HttpRequestInstance.delete(`/api/books/remove-wishlist/${book_id}`);
            if (!response){
                throw new Error('Failed to remove the book from wishlist');
            }
            return response.data;
        } catch (error) {
            return rejectWithValue(error.message);
        }
    }
 );