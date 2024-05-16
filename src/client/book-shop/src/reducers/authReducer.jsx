import { createSlice } from '@reduxjs/toolkit';
import { login, logout } from '../actions/auth';
import { JWT_TOKEN } from '../constants/constants';

export const authSlice = createSlice({
    name: 'auths',
    initialState: {
        token: null,
        loading: false,
        error: null,
        isAuthenticated: false
    },
    reducers: {
        // Reducer logic for other sync actions can be defined here
    },
    extraReducers: (builder) => {
        builder
            .addCase(login.pending, (state) => {
                state.loading = true;
                state.error = null;
                state.isAuthenticated = false;
            })
            .addCase(login.fulfilled, (state, action) => {
                state.loading = false;
                state.token = action.payload;
                localStorage.setItem(JWT_TOKEN, action.payload);
                state.isAuthenticated = true;
            })
            .addCase(login.rejected, (state, action) => {
                state.loading = false;
                state.isAuthenticated = false;
                state.error = action.payload;
            }).addCase(logout.pending, (state) => {
                state.loading = true;
                state.error = null;
                state.isAuthenticated = false;
            })
            .addCase(logout.fulfilled, (state, action) => {
                state.loading = false;
                state.token = null;
                localStorage.removeItem(JWT_TOKEN);
                state.isAuthenticated = false;
            })
            .addCase(logout.rejected, (state, action) => {
                state.loading = false;
                state.isAuthenticated = false;
                state.error = action.payload;
            });;
    }
});

export default authSlice.reducer;
