import { createSlice } from '@reduxjs/toolkit';
import { fetchCategories, fetchCategories4ddl } from '../actions/categories';

export const categoriesSlice = createSlice({
    name: 'categories',
    initialState: {
        items: [],
        ddlItems: [],
        loading: false,
        ddlLoading: false,
        error: null
    },
    reducers: {
        // Reducer logic for other sync actions can be defined here
    },
    extraReducers: (builder) => {
        builder
            .addCase(fetchCategories.pending, (state) => {
                state.loading = true;
                state.error = null;
            })
            .addCase(fetchCategories.fulfilled, (state, action) => {
                state.loading = false;
                state.items = action.payload;
            })
            .addCase(fetchCategories.rejected, (state, action) => {
                state.loading = false;
                state.error = action.payload;
            }).addCase(fetchCategories4ddl.pending, (state) => {
                state.ddlLoading = true;
                state.error = null;
            })
            .addCase(fetchCategories4ddl.fulfilled, (state, action) => {
                state.ddlLoading = false;
                state.ddlItems = action.payload;
            })
            .addCase(fetchCategories4ddl.rejected, (state, action) => {
                state.ddlLoading = false;
                state.error = action.payload;
            });
    }
});

export default categoriesSlice.reducer;
