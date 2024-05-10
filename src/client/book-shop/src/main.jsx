import React from "react";
import ReactDOM from "react-dom/client";
import store from './store';
import { Provider } from 'react-redux';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import NotFoundLayout from "./layouts/NotFoundLayout.jsx";
import MainLayout from "./layouts/MainLayout.jsx";
import HomePage from "./containers/client/HomePage.jsx";
import NewPage from "./containers/client/new_page.jsx";
import NotFoundPage from "./containers/client/404.jsx";

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
          <Route path="/" element={<MainLayoutRoute><HomePage /></MainLayoutRoute>} />
          <Route path="/new-page" element={<MainLayoutRoute><NewPage /></MainLayoutRoute>} />
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
