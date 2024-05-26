import { createSlice } from '@reduxjs/toolkit';
import { fetchFeaturedBooks, fetchSearchBooks, fetchBookDetail, fetchBookWishlist, addBookToWishlist, removeBookFromWishlist } from '../actions/books';

export const booksSlice = createSlice({
    name: 'books',
    initialState: {
        featuredBooks: [],
        loadingFeaturedBook: false,
        errorFeaturedBook: null,
        books: [],
        loadingSearchBook: false,
        errorSearchBook: null,
        bookDetail: null,
        loadingbookDetail: false,
        errorbookDetail: null,
        booksWishlist: [],
        loadingbooksWishlist: false,
        errorbooksWishlist: null,
        addWishlistResult: null,
        loadingaddWishlistResult: false,
        erroraddWishlistResult: null,
        removeWishlistResult: null,
        loadingremoveWishlistResult: false,
        errorremoveWishlistResult: null,
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
            }).addCase(fetchSearchBooks.rejected, (state, action) => {
                state.loadingSearchBook = false;
                state.errorSearchBook = action.payload;
            }).addCase(fetchBookDetail.pending, (state) => {
                state.loadingbookDetail = true;
                state.errorbookDetail = null;
            }).addCase(fetchBookDetail.fulfilled, (state, action) => {
                state.loadingbookDetail = false;
                state.bookDetail = action.payload;
            })
            .addCase(fetchBookDetail.rejected, (state, action) => {
                state.loadingbookDetail = false;
                state.errorbookDetail = action.payload;
            }).addCase(fetchBookWishlist.pending, (state) => {
                state.loadingbooksWishlist = true;
                state.errorbooksWishlist = null;
            }).addCase(fetchBookWishlist.fulfilled, (state, action) => {
                state.loadingbooksWishlist = false;
                state.booksWishlist = action.payload;
            })
            .addCase(fetchBookWishlist.rejected, (state, action) => {
                state.loadingbooksWishlist = false;
                state.errorbooksWishlist = action.payload;
            }).addCase(addBookToWishlist.pending, (state) => {
                state.loadingaddWishlistResult = true;
                state.erroraddWishlistResult = null;
            }).addCase(addBookToWishlist.fulfilled, (state, action) => {
                state.loadingaddWishlistResult = false;
                state.addWishlistResult = action.payload;
            })
            .addCase(addBookToWishlist.rejected, (state, action) => {
                state.loadingaddWishlistResult = false;
                state.erroraddWishlistResult = action.payload;
            }).addCase(removeBookFromWishlist.pending, (state) => {
                state.loadingremoveWishlistResult = true;
                state.errorremoveWishlistResult = null;
            }).addCase(removeBookFromWishlist.fulfilled, (state, action) => {
                state.loadingremoveWishlistResult = false;
                state.removeWishlistResult = action.payload;
            })
            .addCase(removeBookFromWishlist.rejected, (state, action) => {
                state.loadingremoveWishlistResult = false;
                state.errorremoveWishlistResult = action.payload;
            });
    }
});

export default booksSlice.reducer;
