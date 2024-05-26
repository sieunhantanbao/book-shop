import React, { useEffect } from "react";
import { useDispatch } from 'react-redux';
import { logout } from "../../actions/auth";
import { useNavigate } from 'react-router-dom';
function LogoutPage() {

    const dispatch = useDispatch();
    const navigationTo = useNavigate();

    useEffect(() => {
        dispatch(logout());
        navigationTo('/');
    }, [dispatch]);

    return (
        <>
            <h5>Please wait, we are logging you out....</h5>
        </>
    );
}
export default LogoutPage;