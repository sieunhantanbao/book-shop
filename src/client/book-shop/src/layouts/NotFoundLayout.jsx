import React, { useEffect } from 'react';

function NotFoundLayout({ children }) {
    useEffect(() => {
        const loadCSS = async () => {
            await import('./NotFoundLayout.css');
        };
        loadCSS();
        return () => {
            // Optional: Remove CSS if possible or overwrite it in unmount
        };
    }, []);

    return <>{children}</>;
}
export default NotFoundLayout;