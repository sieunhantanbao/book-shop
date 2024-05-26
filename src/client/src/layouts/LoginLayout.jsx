import React, { useEffect } from 'react';

function LoginLayout({ children }) {
  useEffect(() => {
    // Load private CSS
    const loadCSS = async () => {
        await import('./LoginLayout.css');
    };
    loadCSS();

    // Load public CSS
    const cssLinks = [
      "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
      "//code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
      "/client/css/site.css",
      "/client/css/dashboard.css"
    ];

    const cssElements = cssLinks.map(link => {
      const linkElement = document.createElement('link');
      linkElement.rel = 'stylesheet';
      linkElement.href = link;
      document.head.appendChild(linkElement);
      return linkElement;
    });

    // Load public JavaScript
    const jsScripts = [
      "https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js",
      "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js",
      "https://cdn.jsdelivr.net/npm/feather-icons@4.28.0/dist/feather.min.js",
      "https://cdn.jsdelivr.net/npm/chart.js@2.9.4/dist/Chart.min.js",
      "https://code.jquery.com/jquery-3.6.0.js",
      "https://code.jquery.com/ui/1.13.2/jquery-ui.js"
    ];

    const jsElements = jsScripts.map(src => {
      const scriptElement = document.createElement('script');
      scriptElement.src = src;
      scriptElement.async = true;
      document.body.appendChild(scriptElement);
      return scriptElement;
    });

    return () => {
      // Cleanup: Remove the added CSS and JavaScript when unmounting
      cssElements.forEach(element => document.head.removeChild(element));
      jsElements.forEach(element => document.body.removeChild(element));
    };
  }, []);

    return (
        <div className="container">
            {children}
        </div>
    );
}

export default LoginLayout;