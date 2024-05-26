import React from 'react';

function Footer() {
  return (
    <footer className="text-center text-lg-start text-white" style={{ backgroundColor: '#5a5d63' }}>
      {/* Grid container */}
      <div className="container p-4 pb-0">
        {/* Section: Links */}
        <section>
          {/* Grid row */}
          <div className="row">
            {/* Grid column */}
            <div className="col-md-3 col-lg-3 col-xl-3 mx-auto mt-3">
              <h6 className="text-uppercase mb-4 font-weight-bold">
                BookStore
              </h6>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam auctor ante id enim rutrum interdum. Fusce condimentum nisl orci, vitae dapibus lorem elementum ut. Suspendisse mollis metus a lectus elementum varius. Pellentesque tempor massa lorem, non fringilla nunc tempor finibus. Vestibulum commodo sapien ac lobortis venenatis.
              </p>
            </div>
            {/* Grid column */}

            <hr className="w-100 clearfix d-md-none" />

            {/* Grid column */}
            <div className="col-md-3 col-lg-2 col-xl-2 mx-auto mt-3">
              <h6 className="text-uppercase mb-4 font-weight-bold">
                Useful links
              </h6>
              <p><a className="text-white" href="/">Home</a></p>
              <p><a className="text-white" href="/admin/" target="_blank">Administrator</a></p>
              <p><a className="text-white" href="/auth/profile">My profile</a></p>
              <p><a className="text-white" href="/book/wishlist">My wishlist</a></p>
            </div>

            {/* Grid column */}
            <hr className="w-100 clearfix d-md-none" />

            {/* Grid column */}
            <div className="col-md-4 col-lg-3 col-xl-3 mx-auto mt-3">
              <h6 className="text-uppercase mb-4 font-weight-bold">Contact</h6>
              <p><i className="fas fa-home mr-3"></i> New York, NY 10012, US</p>
              <p><i className="fas fa-envelope mr-3"></i> info@gmail.com</p>
              <p><i className="fas fa-phone mr-3"></i> + 01 234 567 88</p>
              <p><i className="fas fa-print mr-3"></i> + 01 234 567 89</p>
            </div>
            {/* Grid column */}
          </div>
          {/*Grid row*/}
        </section>
        {/* Section: Links */}

        <hr className="my-3" />

        {/* Section: Copyright */}
        <section className="p-3 pt-0">
          <div className="row d-flex align-items-center">
            {/* Grid column */}
            <div className="col-md-7 col-lg-8 text-center text-md-start">
              <div className="p-3">
                © 2024 Copyright:
                <a className="text-white" href="/">my-book-store.com</a>
              </div>
            </div>
            {/* Grid column */}

            {/* Grid column */}
            <div className="col-md-5 col-lg-4 ml-lg-0 text-center text-md-end">
              {/* Social Icons */}
              <a className="btn btn-outline-light btn-floating m-1" role="button">
                <i className="fab fa-facebook-f"></i>
              </a>
              <a className="btn btn-outline-light btn-floating m-1" role="button">
                <i className="fab fa-twitter"></i>
              </a>
              <a className="btn btn-outline-light btn-floating m-1" role="button">
                <i className="fab fa-google"></i>
              </a>
              <a className="btn btn-outline-light btn-floating m-1" role="button">
                <i className="fab fa-instagram"></i>
              </a>
            </div>
            {/* Grid column */}
          </div>
        </section>
        {/* Section: Copyright */}
      </div>
      {/* Grid container */}
    </footer>
  );
}

export default Footer;
