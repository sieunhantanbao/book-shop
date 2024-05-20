import UserDetails from "../models/UserDetail"
import { JWT_TOKEN, MY_USER_PROFILE } from "../constants/constants"
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

export function getMyUserProfile() {
    var myUserProfile = localStorage.getItem(MY_USER_PROFILE);
    if(myUserProfile){
        return new MyUserProfile(myUserProfile);
    }
    return null;
}