import { useState } from 'react'

function Header() {
  const isAuthenticated = true;

  return (
    <>
        <header className="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
        <a className="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="/">Book shop</a>
        <button className="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>
        <input className="form-control form-control-dark" type="text" placeholder="Search" aria-label="Search" />
        
        {(() => {
            if (isAuthenticated) {
                return (
                    <div className="col-md-1 col-lg-1 me-0 px-1">
                    <div className="nav-item text-nowrap">
                    <div className="dropdown">
                        {/* <a href="#" className="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                            {% if user.photo_url != None and user.photo_url !='' %}
                            <img src="{{ url_for('static', filename = 'files_uploaded/' + user.photo_url) }}" height="32" width="32" className="rounded-circle me-2" alt="{{ user.email }}">
                            {% else %}
                            <img src="{{ url_for('static', filename = 'admin/dist/img/no-image.png') }}" height="32" width="32" className="rounded-circle me-2" alt="{{ user.email }}">
                            {% endif %}
                            <strong>{{ user.first_name }} {{ user.last_name }}</strong>
                        </a> */}
                        <ul className="dropdown-menu dropdown-menu-dark text-small shadow" style={{ minWidth: '9.2rem' }} aria-labelledby="dropdownUser1">
                            <li><a className="dropdown-item" href="/auth/profile">Profile</a></li>
                            <li><a className="dropdown-item" href="/auth/change-password">Change Password</a></li>
                            <li><hr className="dropdown-divider" /></li>
                            <li><a className="dropdown-item" href="/book/wishlist">My Wishlists</a></li>
                            <li><hr className="dropdown-divider" /></li>
                            <li><a className="dropdown-item" href="/admin/" target="_blank">Admin site</a></li>
                            <li><hr className="dropdown-divider" /></li>
                            <li><a className="dropdown-item" href="/auth/logout">Sign out</a></li>
                        </ul>
                    </div>
                    </div>
                    </div>
                )
            } else {
                return (
                    <div className="navbar-nav">
                    <div className="nav-item text-nowrap">
                    <a className="nav-link px-3" href="/auth/login">Sign In</a>
                    </div>
                    </div>
                )
            }
        })()}
        </header>
    </>
  )
}

export default Header
