import { createSlice } from '@reduxjs/toolkit';
import { fetchCategories, fetchCategories4ddl, fetchCategoryDetail } from '../actions/categories';

export const categoriesSlice = createSlice({
    name: 'categories',
    initialState: {
        items: [],
        loading: false,
        error: null,
        ddlItems: [],
        ddlLoading: false,
        category: null,
        loadingCategory: false,
        errorCategory: null
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
            }).addCase(fetchCategoryDetail.pending, (state) => {
                state.loadingCategory = true;
                state.errorCategory = null;
            })
            .addCase(fetchCategoryDetail.fulfilled, (state, action) => {
                state.loadingCategory = false;
                state.category = action.payload;
            })
            .addCase(fetchCategoryDetail.rejected, (state, action) => {
                state.loadingCategory = false;
                state.errorCategory = action.payload;
            });
    }
});

export default categoriesSlice.reducer;
