import UserDetails from "../models/UserDetail"
import { JWT_TOKEN } from "../constants/constants"
import { jwtDecode } from "jwt-decode";

export function getUserDetails() {
    var token = localStorage.getItem(JWT_TOKEN);
    if(token){
        var decodedToken = jwtDecode(token);
        return new UserDetails(decodedToken);
    }
    return null;
}