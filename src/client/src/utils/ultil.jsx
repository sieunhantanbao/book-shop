import UserDetails from "../models/UserDetail"
import { API_URL, JWT_TOKEN } from "../constants/constants"
import { jwtDecode } from "jwt-decode";
import MyUserProfile from "../models/MyUserProfile";

export function getUserDetails() {
    var token = localStorage.getItem(JWT_TOKEN);
    if (token) {
        var decodedToken = jwtDecode(token);
        return new UserDetails(decodedToken);
    }
    return null;
}

export function convertToMyUserProfile(response) {
    if (response) {
        return new MyUserProfile(response);
    }
    return null;
}

export function getApiUrl() {
    var apiUrl = sessionStorage.getItem(API_URL);
    if (!apiUrl) {
        loadConfig().then((response) => {
            return response;
        });
    } else {
        return apiUrl;
    }
}

// Function to load the config.json file
export async function loadConfig() {
    const response = await fetch('/config.json');
    const config = await response.json();
    sessionStorage.setItem(API_URL, config.API_URL);
    return config.API_URL;
}
