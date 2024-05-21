import UserDetails from "../models/UserDetail"
import { JWT_TOKEN } from "../constants/constants"
import { jwtDecode } from "jwt-decode";
import MyUserProfile from "../models/MyUserProfile";

export function getUserDetails() {
    var token = localStorage.getItem(JWT_TOKEN);
    if(token){
        var decodedToken = jwtDecode(token);
        return new UserDetails(decodedToken);
    }
    return null;
}

export function convertToMyUserProfile(response) {
    if(response){
        return new MyUserProfile(response);
    }
    return null;
}