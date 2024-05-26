import React, { useEffect } from 'react';

function AdminLayout({ children }) {
  useEffect(() => {
    // Load admin CSS
    const cssLinks = [
      "https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback",
      "/admin/plugins/fontawesome-free/css/all.min.css",
      "/admin/plugins/overlayScrollbars/css/OverlayScrollbars.min.css",
      "/admin/plugins/datatables-bs4/css/dataTables.bootstrap4.min.css",
      "/admin/plugins/datatables-responsive/css/responsive.bootstrap4.min.css",
      "/admin/plugins/datatables-buttons/css/buttons.bootstrap4.min.css",
      "/admin/dist/css/adminlte.min.css",
      "/admin/dist/css/dropzone.css",
      "/admin/plugins/summernote/summernote-bs4.min.css",
      "/admin/dist/css/site.css",
      "//code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css",
      "https://cdn.jsdelivr.net/npm/bootstrap5-toggle@5.0.4/css/bootstrap5-toggle.min.css"
    ];

    const cssElements = cssLinks.map(link => {
      const linkElement = document.createElement('link');
      linkElement.rel = 'stylesheet';
      linkElement.href = link;
      document.head.appendChild(linkElement);
      return linkElement;
    });

    // Load admin JavaScript
    const jsScripts = [
      "/admin/plugins/jquery/jquery.min.js",
      "https://code.jquery.com/ui/1.13.2/jquery-ui.js",
      "https://cdn.jsdelivr.net/npm/jquery-validation@1.19.5/dist/jquery.validate.min.js",
      "/admin/plugins/bootstrap/js/bootstrap.bundle.min.js",
      "/admin/plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js",
      "/admin/dist/js/adminlte.min.js",
      "/admin/plugins/jquery-mousewheel/jquery.mousewheel.js",
      "/admin/plugins/raphael/raphael.min.js",
      "/admin/plugins/jquery-mapael/jquery.mapael.min.js",
      "/admin/plugins/jquery-mapael/maps/usa_states.min.js",
      "/admin/plugins/chart.js/Chart.min.js",
      "/admin/plugins/summernote/summernote-bs4.min.js",
      "/admin/dist/js/dropzone-min.js",
      "/admin/plugins/datatables/jquery.dataTables.min.js",
      "/admin/plugins/datatables-bs4/js/dataTables.bootstrap4.min.js",
      "/admin/plugins/datatables-responsive/js/dataTables.responsive.min.js",
      "https://cdn.jsdelivr.net/npm/bootstrap5-toggle@5.0.4/js/bootstrap5-toggle.jquery.min.js",
      "/admin/dist/js/demo.js",
      "/admin/dist/js/pages/dashboard2.js",
      "/admin/dist/js/site.js"
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

  return <div>{children}</div>;
}

export default AdminLayout;
