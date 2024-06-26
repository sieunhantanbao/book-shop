import { createSlice } from '@reduxjs/toolkit';
import { changePassword, getMyProfile, login, logout, registerUser, refreshToken } from '../actions/auth';
import { JWT_TOKEN, JWT_REFRESH_TOKEN } from '../constants/constants';

export const authSlice = createSlice({
    name: 'auths',
    initialState: {
        token: null,
        loading: false,
        error: null,
        loadingRefreshToken: false,
        errorRefreshToken: null,
        isAuthenticated: false,
        registerUserResult: null,
        loadingRegisterUserResult: false,
        errorRegisterUserResult: null,
        changePasswordResultStatus: null,
        changePasswordResultMessage: null,
        loadingChangePasswordResult: false,
        loadingMyProfileResult: false,
        errorMyProfileResult: null
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
            }).addCase(login.fulfilled, (state, action) => {
                state.loading = false;
                state.token = action.payload.access_token;
                localStorage.setItem(JWT_TOKEN, action.payload.access_token);
                localStorage.setItem(JWT_REFRESH_TOKEN, action.payload.refresh_token);
                state.isAuthenticated = true;
            }).addCase(login.rejected, (state, action) => {
                state.loadingRefreshToken = false;
                state.isAuthenticated = false;
                state.errorRefreshToken = action.payload;
            }).addCase(refreshToken.pending, (state) => {
                state.loadingRefreshToken = true;
                state.errorRefreshToken = null;
                state.isAuthenticated = false;
            }).addCase(refreshToken.fulfilled, (state, action) => {
                state.loadingRefreshToken = false;
                state.token = action.payload.access_token;
                localStorage.setItem(JWT_TOKEN, action.payload.access_token);
                localStorage.setItem(JWT_REFRESH_TOKEN, action.payload.refresh_token);
                state.isAuthenticated = true;
            }).addCase(refreshToken.rejected, (state, action) => {
                state.loading = false;
                state.isAuthenticated = false;
                state.error = action.payload;
            })
            .addCase(logout.pending, (state) => {
                state.loading = true;
                state.error = null;
                state.isAuthenticated = false;
            }).addCase(logout.fulfilled, (state, action) => {
                state.loading = false;
                state.token = null;
                localStorage.removeItem(JWT_TOKEN);
                localStorage.removeItem(JWT_REFRESH_TOKEN);
                state.isAuthenticated = false;
            }).addCase(logout.rejected, (state, action) => {
                state.loading = false;
                state.isAuthenticated = false;
                state.error = action.payload;
            }).addCase(registerUser.pending, (state) => {
                state.loadingRegisterUserResult = true;
                state.errorRegisterUserResult = null;
            }).addCase(registerUser.fulfilled, (state, action) => {
                state.loadingRegisterUserResult = false;
                state.registerUserResult = action.payload;
            }).addCase(registerUser.rejected, (state, action) => {
                state.loadingRegisterUserResult = false;
                state.errorRegisterUserResult = action.payload;
            }).addCase(changePassword.pending, (state) => {
                state.loadingChangePasswordResult = true;
            })
            .addCase(changePassword.fulfilled, (state, action) => {
                state.loadingChangePasswordResult = false;
                state.changePasswordResultStatus = action.payload.status;
            })
            .addCase(changePassword.rejected, (state, action) => {
                state.loadingChangePasswordResult = false;
                state.changePasswordResultStatus = action.payload?.status;
                state.changePasswordResultMessage = action.payload?.message;
            }).addCase(getMyProfile.pending, (state) => {
                state.loadingMyProfileResult = true;
                state.errorMyProfileResult = null;
            })
            .addCase(getMyProfile.fulfilled, (state, action) => {
                state.loadingMyProfileResult = false;
            })
            .addCase(getMyProfile.rejected, (state, action) => {
                state.loadingMyProfileResult = false;
                state.errorMyProfileResult = action.payload;
            });
    }
});

export default authSlice.reducer;
