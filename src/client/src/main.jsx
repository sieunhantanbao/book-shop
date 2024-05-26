import React from "react";
import ReactDOM from "react-dom/client";
import store from './store';
import { Provider } from 'react-redux';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NotFoundLayout from "./layouts/NotFoundLayout.jsx";
import HomePage from "./containers/client/HomePage.jsx";
import BookDetailPage from "./containers/client/BookDetailPage.jsx";
import NotFoundPage from "./containers/client/404.jsx";
import BookCategoryPage from "./containers/client/BookCategoryPage.jsx";
import BookCategoryDetailPage from "./containers/client/BookCategoryDetailPage.jsx";
import LoginLayout from "./layouts/LoginLayout.jsx";
import LoginPage from "./containers/auth/LoginPage.jsx";
import LogoutPage from "./containers/auth/LogoutPage.jsx";
import BookWishlistPage from "./containers/client/BookWishlistPage.jsx";
import RegisterUserPage from "./containers/auth/RegisterUserPage.jsx";
import ChangePasswordPage from "./containers/auth/ChangePasswordPage.jsx";
import MyProfilePage from "./containers/auth/MyProfilePage.jsx";
import AdminLayout from "./layouts/AdminLayout.jsx";
import AdminHomePage from "./containers/admin/AdminHomePage.jsx";
import PublicLayout from "./layouts/PublicLayout.jsx";

const LoginLayoutRoute = ({ children }) => {
  return <LoginLayout>{children}</LoginLayout>;
};

const NotFoundLayoutRoute = ({ children }) => {
  return <NotFoundLayout>{children}</NotFoundLayout>;
};

const PublicLayoutRoute = ({ children }) => {
  return <PublicLayout>{children}</PublicLayout>;
};
const AdminLayoutRoute = ({ children }) => {
  return <AdminLayout>{children}</AdminLayout>;
};

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          {/*Public routes*/}
          <Route path="/auth/login" element={<LoginLayoutRoute><LoginPage /></LoginLayoutRoute>} />
          <Route path="/auth/register" element={<LoginLayoutRoute><RegisterUserPage /></LoginLayoutRoute>} />
          <Route path="/auth/logout" element={<LoginLayoutRoute><LogoutPage /></LoginLayoutRoute>} />
          <Route path="/auth/change-password" element={<PublicLayoutRoute><ChangePasswordPage /></PublicLayoutRoute>} />
          <Route path="/auth/profile" element={<PublicLayoutRoute><MyProfilePage /></PublicLayoutRoute>} />
          <Route path="/" element={<PublicLayoutRoute><HomePage /></PublicLayoutRoute>} />
          <Route path="/book/detail/:book_id" element={<PublicLayoutRoute><BookDetailPage /></PublicLayoutRoute>} />
          <Route path="/book/categories/all" element={<PublicLayoutRoute><BookCategoryPage /></PublicLayoutRoute>} />
          <Route path="/book/categories/detail/:cat_id" element={<PublicLayoutRoute><BookCategoryDetailPage /></PublicLayoutRoute>} />
          <Route path="/book/wishlist" element={<PublicLayoutRoute><BookWishlistPage /></PublicLayoutRoute>} />
          {/*Admin routes*/}
          <Route path="/admin/" element={<AdminLayoutRoute><AdminHomePage /></AdminLayoutRoute>} />
          {/*Not found route*/}
          <Route path="*" element={<NotFoundLayoutRoute><NotFoundPage /></NotFoundLayoutRoute>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Provider store={store}>
        <App />
  </Provider>
);
