import React from "react";
import ReactDOM from "react-dom/client";
import store from './store';
import { Provider } from 'react-redux';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NotFoundLayout from "./layouts/NotFoundLayout.jsx";
import MainLayout from "./layouts/MainLayout.jsx";
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

const LoginLayoutRoute = ({ children }) => {
  return <LoginLayout>{children}</LoginLayout>;
};

const NotFoundLayoutRoute = ({ children }) => {
  return <NotFoundLayout>{children}</NotFoundLayout>;
};

const MainLayoutRoute = ({ children }) => {
  return <MainLayout>{children}</MainLayout>;
};

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/auth/login" element={<LoginLayoutRoute><LoginPage /></LoginLayoutRoute>} />
          <Route path="/auth/register" element={<LoginLayoutRoute><RegisterUserPage /></LoginLayoutRoute>} />
          <Route path="/auth/logout" element={<LoginLayoutRoute><LogoutPage /></LoginLayoutRoute>} />
          <Route path="/auth/change-password" element={<MainLayoutRoute><ChangePasswordPage /></MainLayoutRoute>} />
          <Route path="/auth/profile" element={<MainLayoutRoute><MyProfilePage /></MainLayoutRoute>} />
          <Route path="/" element={<MainLayoutRoute><HomePage /></MainLayoutRoute>} />
          <Route path="/book/detail/:book_id" element={<MainLayoutRoute><BookDetailPage /></MainLayoutRoute>} />
          <Route path="/book/categories/all" element={<MainLayoutRoute><BookCategoryPage /></MainLayoutRoute>} />
          <Route path="/book/categories/detail/:cat_id" element={<MainLayoutRoute><BookCategoryDetailPage /></MainLayoutRoute>} />
          <Route path="/book/wishlist" element={<MainLayoutRoute><BookWishlistPage /></MainLayoutRoute>} />
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
