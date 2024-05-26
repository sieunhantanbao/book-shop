class UserDetails {
    constructor(response) {
        this.user_id = response.id ? response.id : null;
        this.email = response.sub ? response.sub : null;
        this.first_name = response.first_name ? response.first_name : null;
        this.last_name = response.last_name ? response.last_name : null;
        this.is_admin = response.is_admin ? response.is_admin : false;
        this.is_active = response.is_active ? response.is_active : false;
    }
}

export default UserDetails;

