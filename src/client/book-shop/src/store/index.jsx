import { configureStore } from '@reduxjs/toolkit';
import categoriesReducer from '../reducers/categoriesReducer';
import booksReducer from '../reducers/booksReducer';

const store = configureStore({
    reducer: {
        categories: categoriesReducer,
        books: booksReducer
    },
});

export default store;
