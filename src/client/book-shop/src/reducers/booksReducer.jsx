import { createSlice } from '@reduxjs/toolkit';
import { fetchFeaturedBooks, fetchSearchBooks } from '../actions/books';

export const booksSlice = createSlice({
    name: 'books',
    initialState: {
        featuredBooks: [],
        books: [],
        loadingFeaturedBook: false,
        loadingSearchBook: false,
        errorFeaturedBook: null,
        errorSearchBook: null
    },
    reducers: {
        // Reducer logic for other sync actions can be defined here
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchFeaturedBooks.pending, (state) => {
                state.loadingFeaturedBook = true;
                state.errorFeaturedBook = null;
            })
            .addCase(fetchFeaturedBooks.fulfilled, (state, action) => {
                state.loadingFeaturedBook = false;
                state.featuredBooks = action.payload;
            })
            .addCase(fetchFeaturedBooks.rejected, (state, action) => {
                state.loadingFeaturedBook = false;
                state.errorFeaturedBook = action.payload;
            }).addCase(fetchSearchBooks.pending, (state) => {
                state.loadingSearchBook = true;
                state.errorSearchBook = null;
            }).addCase(fetchSearchBooks.fulfilled, (state, action) => {
                state.loadingSearchBook = false;
                state.books = action.payload;
            })
            .addCase(fetchSearchBooks.rejected, (state, action) => {
                state.loadingSearchBook = false;
                state.errorSearchBook = action.payload;
            });
    }
});

export default booksSlice.reducer;
