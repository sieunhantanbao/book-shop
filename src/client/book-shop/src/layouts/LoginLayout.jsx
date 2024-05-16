import React, { useEffect } from 'react';

function LoginLayout({ children }) {
    useEffect(() => {
        const loadCSS = async () => {
            await import('./LoginLayout.css');
        };
        loadCSS();
        return () => {
            // Optional: Remove CSS if possible or overwrite it in unmount
        };
    }, []);

    return (
        <div className="container">
             {children}
        </div>
    )
}
export default LoginLayout;