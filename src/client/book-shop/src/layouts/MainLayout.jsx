import React from "react";
import Header from "../components/common/Header";
import Footer from "../components/common/Footer";

const MainLayout = ({ children }) => {
  return (
    <>
    <Header />
        <div className="container">
            <div className="row">
                <main className="col-md-12 ms-sm-auto col-lg-12 px-md-4">
                    {children}
                </main>
            </div>
        </div>
    <Footer />
    </>
  );
};

export default MainLayout;
