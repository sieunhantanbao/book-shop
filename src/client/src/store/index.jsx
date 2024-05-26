import { configureStore } from '@reduxjs/toolkit';
import categoriesReducer from '../reducers/categoriesReducer';
import booksReducer from '../reducers/booksReducer';
import authReducer from '../reducers/authReducer';

const store = configureStore({
    reducer: {
        categories: categoriesReducer,
        books: booksReducer,
        auths: authReducer
    },
});

export default store;
